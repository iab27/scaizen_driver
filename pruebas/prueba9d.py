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

#result=client.read_holding_registers(1134,2,unit=1)
#result=client.read_input_registers(1134,2,unit=0x01)
#result=client.register_write_message.WriteSingleregisterRequest(1134,500,unit=0x01)
result=client.read_holding_registers(1134,2,unit=0x01)
#result=client.read_holding_registers(1132,2,unit=0x01)
#print(result.registers)
#response=client.execute(result)
#print(result.registers)
#result=client.write_register(1132,False,unit=0x01)
#result=client.read_coils(1134,2,unit=0x01)
print(result.registers)
#result=client.read_holding_registers(1134,2,unit=1)
#print(result.registers)
#print('Brillo de pantalla (500-10000, %): ',result.registers[0])



client.close()
