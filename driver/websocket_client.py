#!/usr/bin/env python
from tornado.websocket import websocket_connect
import asyncio
import json

import argparse
import sys
import base64

# import logging
# # Enable logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

MENSAJE_JSON = False

#se obtiene el mensaje del primer argumento
parser = argparse.ArgumentParser()
parser.add_argument('mensaje', type=str)
args = parser.parse_args()
msg = args.mensaje
if MENSAJE_JSON:
    json = msg.decode('ascii')
else:
    #mensaje codificado con base64
    mensaje64 = args.mensaje
    mensaje64_bytes = mensaje64.encode('ascii')
    message_bytes = base64.b64decode(mensaje64_bytes)
    json = message_bytes.decode('ascii')
# logger.info(json)

async def main():
    url = "ws://localhost:5500/patin"
    try:
        conn = await websocket_connect(url)
        await conn.write_message(json)
    except ConnectionRefusedError:
        print('error: ConnectionRefusedError')
        sys.exit(1)
    except TimeoutError:
        print('error: TimeoutError')
        sys.exit(1)
    print('done')
    sys.exit(0)

asyncio.run(main())
