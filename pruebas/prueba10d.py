from pymodbus.client.sync import ModbusTcpClient
#from pymodbus.register_read_message import ReadHoldingRegistersResponse

import logging

def listToString(s):
	str1=''
	for ele in s:
		str1+=chr(ele)
	return str1

logging.basicConfig()
log=logging.getLogger()
#log.setLevel(logging.DEBUG)

client=ModbusTcpClient('192.168.0.200')
client.connect()

result=client.read_holding_registers(7800,1,unit=1)
print(result.registers)

result=client.read_holding_registers(7801,1,unit=1)
print(result)

result=client.read_holding_registers(7810,2,unit=1)
print(result)

result=client.read_holding_registers(7817,25,unit=1)
print(result)

result=client.read_holding_registers(7842,25,unit=1)
print(result)

result=client.read_holding_registers(7867,25,unit=1)
print(result)

result=client.read_holding_registers(7892,25,unit=1)
print(result)

#if not result.isError():
#	print('Exito: ')
#	print(result.registers)
#	print(listToString(result.registers))
#else:
#	print('Error: {}'.format(result.registers))

client.close()
