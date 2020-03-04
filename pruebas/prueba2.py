import os
from pymodbus.client.sync import ModbusTcpClient

cliente = ModbusTcpClient('192.168.0.200','443')


print("Read Coils")
#request = cliente.read_coils(0x0,0x8,unit=1)
request = cliente.read_coils(0x173,0x174,unit=1)
print(request)
#print(request.bits[0])
#print(request.bits[1])
#print(request.bits[2])
#print(request.bits[3])
#print(request.bits[4])
#print(request.bits[5])
#print(request.bits[6])
#print(request.bits[7])
