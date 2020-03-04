#!/usr/bin/env python

# import redis
import logging
import redis_db

db = redis_db.RedisConnection()
db.deleteAll()

# bitacora = redis_db.RedisTable('scaizen', 'bitacora', ['id', 'id_externo'])
# bitacora.all()
# 
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
