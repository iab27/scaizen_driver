#!/usr/bin/python3           
# This is client.py file

import socket
import struct
import time

# Create a TCP/IP socket
TCP_IP = '192.168.0.200'
TCP_PORT = 502
BUFFER_SIZE = 39
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

try:

    unitId = 1
    functionCode =6
    print("\n,Switching plug on")
    coilId = 1
    req = struct.pack('12B', 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, int(unitId), int(functionCode), 0x00, 0x46, 0x0B, 0x0B)
    sock.send(req)
    print("TX: (%s)" % req)


    time.sleep(2)

finally:
    print('\nCLOSING SOCKET')
    sock.close()
