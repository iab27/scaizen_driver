# -*- coding: utf-8 -*-
"""
Created on feb 2020

@author:  @watermarkero
"""
#!/usr/bin/python
from uuid import uuid4
from datetime import datetime
import redis
import logging
import redis_db


def getNow():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def getNow4Index():
    return datetime.now().strftime('%Y%m-%d%H-%M%S-')


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def nueva_tarea_ucl_rt(json_txt):
    bitacora = redis_db.RedisTable('scaizen', 'bitacora', ['id', 'id_externo'])
    if bitacora == None:
        return ''
    registro = {}
    registro['id'] = getNow4Index() + str(uuid4())
    registro['fecha_creacion'] = getNow()
    registro['id_externo'] = registro['id']
    registro['tarea_mensaje'] = json_txt
    registro['worker_estado_encola'] = 1
    registro['worker_tarea_duracion'] = 3
    registro['worker_tarea_tipo'] = 'scaizen_ucl_rt'
    registro['worker_procesamiento_inicio'] = ''
    registro['worker_procesamiento_fin'] = ''
    registro['worker_estado_enprocesamiento'] = 0
    registro['worker_estado_finalizado_ok'] = 0
    registro['worker_estado_finalizado_error'] = 0
    registro['worker_tarea_output'] = ''

    cola_de_trabajo = redis_db.RedisQueue('scaizen', 'tareas_pendientes_ucl')
    if cola_de_trabajo == None:
        return ''
    # se añade el registro en la bitácora y en la cola de trabajo
    logger.info('se añade el registro en la bitacora...')
    bitacora.insert(registro)
    logger.info('se añade el registro en la cola: ' + registro['id'])
    cola_de_trabajo.put(registro['id'])
    return registro['id']


def iniciar_procesamiento_ucl_rt():
    logger.info('iniciando RedisQueue')
    cola_de_trabajo = redis_db.RedisQueue('scaizen', 'tareas_pendientes_ucl')
    if cola_de_trabajo.empty():
        logger.info('QUEUE vacía')
        return None
    logger.info('iniciando RedisTable')
    bitacora = redis_db.RedisTable('scaizen', 'bitacora', ['id', 'id_externo'])
    if bitacora == None:
        return None
    logger.info('Extrayendo tarea de QUEUE...')
    id_tarea = cola_de_trabajo.get().decode()
    logger.info(id_tarea)
    ret = bitacora.getByIndex('id', id_tarea)
    logger.info(ret)
    if len(ret) == 1:
        registro = ret[0]

    logger.info('Tarea obtenida')
    #se ectualiza la bitácora
    registro_update = {}
    registro_update['worker_procesamiento_inicio'] = getNow()
    registro_update['worker_estado_encola'] = 0
    registro_update['worker_estado_enprocesamiento'] = 1
    bitacora.update('id', id_tarea, registro_update)

    #se retorna la tarea para que el worker la ejecute
    return (registro['id'], registro['worker_tarea_tipo'], registro['tarea_mensaje'], registro_update['worker_procesamiento_inicio'], registro['worker_tarea_duracion'])

def finalizar_procesamiento_ucl_rt(tarea_id, output, error = 0):
    bitacora = redis_db.RedisTable('scaizen', 'bitacora', ['id', 'id_externo'])
    if bitacora == None:
        return None
    #se ectualiza la bitácora
    registro_update = {}
    registro_update['worker_procesamiento_fin'] = getNow()
    registro_update['worker_estado_enprocesamiento'] = 0
    if error == 1:
        registro_update['worker_estado_finalizado_ok'] = 0
        registro_update['worker_estado_finalizado_error'] = 1
    else:
        registro_update['worker_estado_finalizado_ok'] = 1
        registro_update['worker_estado_finalizado_error'] = 0

    registro_update['worker_tarea_output'] = output
    bitacora.update('id', tarea_id, registro_update)
