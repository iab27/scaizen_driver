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

#result=client.read_holding_registers(0x14B4,2,unit=1)

x=4312
result=client.read_holding_registers(x,2,unit=1)
if not result.isError():
	print('Exito: ')
	print(result.registers)
	print('Velocidad de flujo: ',result.registers[0],' l/min')
else:
	print('Error: {}'.format(result))

client.close()
