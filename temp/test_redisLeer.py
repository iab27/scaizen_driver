#!/usr/bin/env python
import logging
import redis_db
from uuid import uuid4
from datetime import datetime

def getNow():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def getNow4Index():
    return datetime.now().strftime('%Y%m-%d%H-%M%S-')


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('conectandose a REDIS...')

#db = redis_db.Redisconnection()

bitacora = redis_db.RedisTable('scaizen', 'bitacora', ['id', 'id_pedido'])

ret = bitacora.getByIndex('id_pedido',1)

if len(ret)==1:
	registro =ret[0]


logger.info(registro)
logger.info(registro['cantidad_programada'])

# redis_server = redis.Redis()
#redis_server = redis.Redis(host='localhost', port=6379, password=None)
#redis_server.rpush('cola', 'otro')
#redis_server.ping()
