from pymodbus.client.sync import ModbusTcpClient

import logging

def listToString(s):
	str1=''
	for ele in s:
		str1+=chr(ele)
	return str1

logging.basicConfig()
log=logging.getLogger()
log.setLevel(logging.DEBUG)

client=ModbusTcpClient('192.168.0.200')
client.connect()

result=client.read_holding_registers(0x00da,25,unit=1)

if not result.isError():
	print('Exito: ')
	print(result.registers)
	print(listToString(result.registers))
else:
	print('Error: {}'.format(results))

client.close()
