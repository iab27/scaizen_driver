# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 23:49:33 2017

@author:  @watermarkero
"""

#!/usr/bin/python
# pip3 install redis
import redis
import logging


def toDict(data):
    data_type = type(data)
    if data_type == bytes:
        return data.decode()
    if data_type in (str, int):
        return str(data)
    if data_type == dict:
        data = data.items()
    return data_type(map(toDict, data))


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class RedisConnection(object):
    r = None

    def __init__(self):
        if not self.is_redis_available():
            self.connect()

    def connect(self, intentos=3):
        conexionExitosa = True
        for i in range(intentos):
            logger.info('conectandose a REDIS  (intento ' +
                        str(i+1)+' de ' + str(intentos) + ')...')
            try:
                RedisConnection.r = redis.Redis(
                    host='localhost', port=6379, password=None)
                conexionExitosa = True
            except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
                logger.info('intento fallido')
                conexionExitosa = False
            if (conexionExitosa == True) and (self.is_redis_available()):
                logger.info('conexión exitosa con REDIS')
                return True
        logger.info('CONEXIÓN FALLIDA CON REDIS')
        return False

    def is_redis_available(self):
        if RedisConnection.r == None:
            logger.info('redis not initiated')
            return False
        try:
            RedisConnection.r.ping()
            logger.info('redis available')
        except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
            logger.info('redis not available')
            return False
        return True

    def deleteAll(self):
        if not self.is_redis_available():
            return -1
        pattern = '*'
        registros = toDict(RedisConnection.r.keys(pattern))
        logger.info('Limpiando REDIS: ' + str(len(registros)))
        for registro in registros:
            RedisConnection.r.delete(registro)

    def getKeys(self, pattern, onlyOne=False):
        if not self.is_redis_available():
            return -1
        if (onlyOne == True):
            redisKey = (toDict(RedisConnection.r.keys(pattern)))[0]
        else:
            redisKey = toDict(RedisConnection.r.keys(pattern))
        logger.info('get key: ' + str(redisKey))
        return redisKey

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RedisTable(RedisConnection):
    def __init__(self, namespace, name, indices=[]):
        self.r = None
        if not super(RedisTable, self).is_redis_available():
            if super(RedisTable, self).connect():
                self.r = RedisConnection.r
        else:
            self.r = RedisConnection.r
            
        if self.r == None:
            logger.info('redis not initiated')
            return None
        self.namespace = namespace
        self.name = name
        self.prefix = self.namespace+':'+'tabla:'+self.name + ':'
        self.registerCounter = self.prefix + 'registerCounter'
        self.indexes = self.prefix + 'indexes'
        # se crea la llave de la tabla
        self.r.setnx(self.registerCounter, 0)
        for indice in indices:
            self.addIndex(indice)
        logger.info('tabla iniciada: ' + self.prefix)

    def addIndexes(self, indices):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        for indice in indices:
            self.addIndex(indice)

    def addIndex(self, name):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        ret = self.r.sadd(self.indexes, name)
        logger.info('indice agregado: ' + name + ', ret='+str(ret))

    def getIndexesFromRegister(self, register):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        lista = []
        campos = register.keys()
        indexes = toDict(self.r.smembers(self.indexes))
        for index in indexes:
            for campo in campos:
                if index == campo:
                    lista.append(index)
        return lista

    def __insertIndex(self, idRegistro, campo, value, registroKey):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        indexKey = self.prefix + 'index:' + \
            str(idRegistro) + ':' + str(campo) + ':' + str(value)
        logger.info('indice insertado: ' + str(indexKey))
        ret = self.r.set(indexKey, registroKey)
        return ret

    """
    insertar un elemento a la tabla.
    registro: es un diccionario de python con los campos, ejemplo:
        registro={}
        registro['nombre']='Juan'
        registro['paterno']='Pérez'
        registro['materno']='García'
        registro['edad']=21    
    """

    def insert(self, registro):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        # se obtiene el key del hash, se incrementa el counter primero
        idRegistro = self.r.incr(self.registerCounter)
        registro['_idRegistro_'] = idRegistro
        keyRegistro = self.prefix + 'registro:' + str(idRegistro)
        ret = self.r.hmset(keyRegistro, registro)
        logger.info('registro insertado: ' + keyRegistro)
        # guardar indices
        indices = self.getIndexesFromRegister(registro)
        for indice in indices:
            self.__insertIndex(idRegistro, indice,
                               registro[indice], keyRegistro)
        return ret, idRegistro, keyRegistro, indices

    def __findRegisterIdbyIndex(self, indexKey, indexValue):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        pattern = self.prefix + 'index:*:' + str(indexKey) + ':' + str(indexValue)
        logger.info('__findRegisterIdbyIndex')
        logger.info(pattern)

        indexes = toDict(self.r.keys(pattern))
        ret = []
        for indexKey in indexes:
            ret.append(self.r.get(indexKey))
        return ret

    # falta probar si se modifica una llave...eliminar la llave anterior y crear la nueva
    def update(self, indexKey, indexValue, registro):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        listOfregisterId = self.__findRegisterIdbyIndex(indexKey, indexValue)
        if len(listOfregisterId) > 0:
            for registerId in listOfregisterId:
                idRegistro = toDict(registerId)
                # por cada id de registro
                registroenEnBd = toDict(self.r.hgetall(idRegistro))
                indicesPormodificar = self.getIndexesFromRegister(registro)
                logger.info('registroenEnBd: ' + idRegistro)
                logger.info(registroenEnBd)

                for indice in indicesPormodificar:
                    # verificar que el indice exista en la bd
                    try:
                        registroExiste = registroenEnBd[indice] is not None
                    except KeyError:
                        registroExiste = False
                    # si existe en bd
                    if registroExiste == True:
                        if registroenEnBd[indice] != registro[indice]:
                            # eliminar el indice:
                            indexKey = self.prefix + 'index:' + \
                                str(registroenEnBd['_idRegistro_']) + ':' + \
                                indice + ':' + str(registroenEnBd[indice])
                            self.r.delete(indexKey)
                            logger.info('indice eliminado: ' + str(indexKey))

                            # actualizar el indice
                            keyRegistro = self.prefix + 'registro:' + \
                                str(registroenEnBd['_idRegistro_'])
                            self.__insertIndex(
                                str(registroenEnBd['_idRegistro_']), indice, registro[indice], keyRegistro)
                    else:
                        # insertar el indice
                        keyRegistro = self.prefix + 'registro:' + \
                            str(registroenEnBd['_idRegistro_'])
                        self.__insertIndex(
                            str(registroenEnBd['_idRegistro_']), indice, registro[indice], keyRegistro)

                ret = self.r.hmset(idRegistro, registro)
                logger.info('update registro: ' + idRegistro)
                indices = self.__findRegisterIdbyIndex(indexKey, indexValue)
                return ret, indices

    def all(self):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        pattern = self.prefix+'registro:*'
        registros = toDict(self.r.keys(pattern))
        logger.info('all registros obtenidos: ' + str(len(registros)))
        logger.info(registros)
        return registros

    def getById(self, id):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        ret = toDict(self.r.hgetall(id))
        logger.info('getById: ')
        logger.info(ret)
        return ret

    def generateRegisterKey(self, idRegistro):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        return self.prefix + 'registro:' + str(idRegistro)

    def getByIndex(self, indexKey, indexValue):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        listOfregisterId = self.__findRegisterIdbyIndex(indexKey, indexValue)
        ret = []
        for registerId in listOfregisterId:
            ret.append(toDict(self.r.hgetall(toDict(registerId))))
        logger.info('getByIndex: ' + str(len(ret)))
        logger.info(ret)
        return ret

    def __deleteKey(self, key):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        return self.r.delete(key)

    def deleteByIndex(self, indexKey, indexValue):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        listOfregisterId = self.__findRegisterIdbyIndex(indexKey, indexValue)
        for registerId in listOfregisterId:
            registro = self.getById(toDict(registerId))
            # eliminar el registro
            self.__deleteKey(toDict(registerId))
            logger.info('registro eliminado: ' + toDict(registerId))
            # eliminar los indices
            pattern = self.prefix + 'index:' + \
                str(registro['_idRegistro_']) + '*'
            indexes = toDict(self.r.keys(pattern))
            for indexKey in indexes:
                self.__deleteKey(toDict(indexKey))
                logger.info('indice eliminado: ' + toDict(indexKey))

    def deleteRegisterById(self, registerId):
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        registerKey = self.generateRegisterKey(registerId)
        # eliminar el registro
        self.__deleteKey(registerKey)
        logger.info('registro eliminado: ' + registerKey)
        # eliminar los indices
        pattern = self.prefix + 'index:' + str(registerId) + '*'
        indexes = toDict(self.r.keys(pattern))
        for indexKey in indexes:
            self.__deleteKey(toDict(indexKey))
            logger.info('indice eliminado: ' + toDict(indexKey))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RedisString(RedisConnection):
    def __init__(self):
        if not super(RedisString, self).is_redis_available():
            super(RedisString, self).connect()
        self.r = RedisConnection.r
        logger.info('string iniciado: ')

    def get(self, key):
        ret = self.r.get(key)
        logger.info('get: ' + ret.decode())
        return ret

    def set(self, key, value):
        ret = self.r.set(key, value)
        logger.info('set: ' + str(ret))
        return ret

    def setnx(self, key, value):
        ret = self.r.setnx(key, value)
        logger.info('setnx: ' + str(ret))
        return ret

    def incr(self, key):
        ret = self.r.incr(key)
        logger.info('incr: ' + str(ret))
        return ret

    def delete(self, key):
        ret = self.r.delete(key)
        logger.info('delete: ' + str(ret))
        return ret

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RedisQueue(RedisConnection):
    def __init__(self, namespace, name):
        self.r = None
        if not super(RedisQueue, self).is_redis_available():
            if super(RedisQueue, self).connect():
                self.r = RedisConnection.r
        else:
            self.r = RedisConnection.r
        if self.r == None:
            logger.info('redis not initiated')
            return None
        self.namespace = namespace
        self.name = self.namespace+':'+'queue:'+name

    def qsize(self):
        """Return the approximate size of the queue."""
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        return self.r.llen(self.name)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        self.r.lpush(self.name, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue. 

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        if block:
            item = self.r.brpop(self.name, timeout=timeout)
        else:
            item = self.r.rpop(self.name)

        if item:
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        if self.r == None:
            logger.info('redis not initiated')
            return -1
        return self.get(False)


# db = RedisConnection()
# db.deleteAll()

# usr = RedisTable('scaizen','usuarios',['id','telefono'])

# pedro={}
# pedro['id']=3
# pedro['nombre']='pedro'
# pedro['paterno']='hdz'
# pedro['materno']='Avalos'
# pedro['telefono']='1234'
# pedro['edad']=90

# # usr.insert(pedro)
# usr.update('id',3, pedro)
# ##
# ret = usr.getByIndex('telefono','1234')
# if len(ret) == 1:
#  usuario = ret[0]
# print(usuario)
# ##
# ##
# usr.all()
# ##
##
# usr.deleteByIndex('id',3)
#
# usr.all()
#
##
#rString = RedisString()
# rString.set('a',2)
# rString.get('a')
# rString.delete('a')
