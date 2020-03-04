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
    functionCode =16
    print("\n,Switching plug on")
    coilId = 1
    req = struct.pack('15B',0x00, 0x01, 0x00, 0x00, 0x00, 0x0a, int(unitId), int(functionCode), 0x04, 0x6c, 0x00, 0x02, 0x02, 0x00, 0x00)
    #Marca direcccion ilegal
    #req = struct.pack('14B',0x00, 0x01, 0x00, 0x00, 0x00, 0x0a, int(unitId), int(functionCode), 0x04, 0x6a, 0x00, 0x01, 0x01, 0x4d)
    #Marca tamanos incorrectos
    #req = struct.pack('15B',0x00, 0x01, 0x00, 0x00, 0x00, 0x09, int(unitId), int(functionCode), 0x04, 0x6a, 0x04, 0x6b, 0x00, 0x4d, 0x09)
    sock.send(req)
    print("TX: (%s)" % req)


    time.sleep(2)

finally:
    print('\nCLOSING SOCKET')
    sock.close()

