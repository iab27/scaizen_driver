# -*- coding: utf-8 -*-
"""
Created on feb 2020

@author:  @watermarkero
"""

#!/usr/bin/python
from asyncproc import Process
import os
import logging
import json
import base64
import asyncio

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def send_message_to_websocket_server(manager,mensaje):
    message_bytes = mensaje.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    #myProc = Process(['python3', 'websocket_client.py', base64_bytes])
    id_process = manager.start(['python3', 'websocket_client.py', base64_bytes])
    return id_process
    # out = myProc.read()
    # respuesta = ''
    # while True:
    #     status = myProc.wait(os.WNOHANG)
    #     if status is not None:
    #         break
    #     out = myProc.read()
    #     if len(out) > 2:
    #         respuesta = respuesta+out.decode().rstrip()
    # return '{"output":"'+respuesta+'", "error": 0}'

