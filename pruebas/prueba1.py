from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.200')
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result[0])
print("Funcionando")
print(client)
client.close()
