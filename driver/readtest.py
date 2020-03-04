#!/usr/bin/env python

#Esto lo agregué
from pymodbus.client.sync import ModbusTcpClient
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
import administracion_de_tareas
import time	 
import os
#import msvcrt

#Esto no lo modifiqué
import logging
import json
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)


#Esto lo agregué
API_ENDPOINT="http://127.0.0.1:5510/endpointdata"
#def listToString(s):
#    str1=''
#    i=0
#    for ele in s:
#        if i<1: str1+=chr(ele)
#        elif i<2:  str1+=chr(ele)+'-'
#        elif i<3:  str1+=chr(ele)
#        elif i<4:  str1+=chr(ele)+'-'
#        elif i<5:  str1+=chr(ele)
#        elif i<6:  str1+=chr(ele)+' '
#        elif i<7:  str1+=chr(ele)
#        elif i<8:  str1+=chr(ele)+':'
#        elif i<9:  str1+=chr(ele)
#        elif i<10: str1+=chr(ele)+':'
#        else:      str1+=chr(ele)
#        i=i+1
#    return str1

def listToString(s):
	str1=''
	for ele in s:
		str1+=chr(ele)
	return str1


#logging.basicConfig()
#log=logging.getLogger()


#hostname = "192.168.0.200" #example
#response = os.system("ping -c 1 " + hostname)
#and then check the response...
#if response == 0:
#  print(hostname, 'is up!')
#else:
#  print(hostname, 'is down!')



#Este codigo se da cuenta si hay o no conexion con la UCL
client=ModbusTcpClient('192.168.0.200')
while 1:
	if client.connect():
		print('Hay conexion')
		client.close()
		time.sleep(1)
	else:
		print('No hay conexion')
		time.sleep(1)	
#while 1:
#	try:
#		client=ModbusTcpClient('192.168.0.200')
#		flag = client.connect()
#		if flag==1:
#			print('Conectado')
#		else:
#	except:
#		print('No hay conexión')
#		time.sleep(5)

#prueba=client.read_holding_registers(1200,10,unit=1)
#print(prueba.registers)


#prueba=client.read_holding_registers(1376,30,unit=1)
#print(prueba.registers)

#prueba=client.read_holding_registers(1760,30,unit=1)
#print(prueba.registers)

#prueba=client.read_holding_registers(1200,20,unit=1)
#print(prueba.registers)
#print(listToString(prueba.registers))


#prueba=client.read_holding_registers(1700,18,unit=1)
#print(prueba.registers)
#print(listToString(prueba.registers))

#client.close()
