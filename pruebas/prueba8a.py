from pymodbus.client.sync import ModbusTcpClient

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

print('*'*37)
print('01 Brazo 01 Componente Estado')
print('*'*37)

#5.1.1. Real-time preset gross totalizer
result=client.read_holding_registers(3000,2,unit=1)
print('Totalizer (preset): ',result.registers[0],' l')

#5.1.2. Real-time meter gross totalizer
result=client.read_holding_registers(3024,2,unit=1)
print('Totalizer (meter): ',result.registers[0],' l')

#5.1.3. Real-time component gross totalizer
result=client.read_holding_registers(3144,2,unit=1)
print('Totalizer (component): ',result.registers[0],' l')

#5.1.5. Real-time preset net totalizer
result=client.read_holding_registers(3720,2,unit=1)
print('Totalizer (preset net): ',result.registers[0],' l')

#5.1.6. Real-time component net totalizer
result=client.read_holding_registers(3744,2,unit=1)
print('Totalizer (component net): ',result.registers[0],' l')

#5.2.1. Preset quantity in whole units
result=client.read_holding_registers(4036,2,unit=1)
print('GOV objetivo (preset quantity in whole): ',result.registers[0],' l')

#5.2.2. Preset delivered gross quantity in whole units
result=client.read_holding_registers(4060,2,unit=1)
print('IV/GSV (preset delivered quantity): ',result.registers[0],' l')

#5.2.3. Preset delivered net quantity in whole units
result=client.read_holding_registers(4084,2,unit=1)
print('IV/GSV (preset delivered net quantity): ',result.registers[0],' l')

#5.2.8. Meter delivered gross quantity in whole units
result=client.read_holding_registers(4192,2,unit=1)
print('IV/GSV (meter delivered gross quantity): ',result.registers[0],' l')

#5.2.10. Component delivered gross quantity in whole units
result=client.read_holding_registers(4372,2,unit=1)
print('IV/GSV (component delivered gross quantity): ',result.registers[0],' l')

#5.2.11. Component delivered net quantity in whole units
result=client.read_holding_registers(4564,2,unit=1)
print('IV/GSV (component delivered net quantity): ',result.registers[0],' l')

#5.2.7. Preset gross flow rate in whole units
result=client.read_holding_registers(4180,2,unit=1)
print('Velocidad de flujo (preset): ',result.registers[0],' l/min')

#5.2.9. Meter gross flow rate in whole units
result=client.read_holding_registers(4312,2,unit=1)
print('Velocidad de flujo (meter): ',result.registers[0],' l/min')

#5.2.13. Component batch average pressure in tenths or hundredths
result=client.read_holding_registers(4948,2,unit=1)
print('Presión (component batch): ',result.registers[0]/100,' KPa')

#5.2.16. Component current pressure in hundredths
result=client.read_holding_registers(4948,2,unit=1)
print('Presión en vivo (component current): ',result.registers[0]/100,' KPa')

#5.2.17. Component current density in tenths
result=client.read_holding_registers(5716,2,unit=1)
print('Densidad actual (component current): ',result.registers[0]/10,' Kg m^3')

#5.2.19. Component current relative density in ten thousands
result=client.read_holding_registers(6292,2,unit=1)
print('Densidad relativa actual (component current): ',result.registers[0]/10,' Kg m^3')

#5.2.14. Component batch average density/relative density/gravity
result=client.read_holding_registers(5140,2,unit=1)
print('Densidad/Relativa Densidad/Gravity (component batch): ',result.registers[0]/10,' Kg m^3')

#5.2.15. Component current temp in hundredths
result=client.read_holding_registers(5332,2,unit=1)
print('Temperatura en vivo (component current): ',result.registers[0]/100,' C')

#5.2.12. Component batch average temp in tenths or hundredths
result=client.read_holding_registers(4756,2,unit=1)
print('Temperatura (component batch): ',result.registers[0]/100,' C')

#5.2.4. Preset batch average temp in tenths or hundredths
result=client.read_holding_registers(4108,2,unit=1)
print('Temperatura promedio (preset batch): ',result.registers[0]/100,' C')

#5.2.22. Component current mass delivered
result=client.read_holding_registers(6868,2,unit=1)
print('Masa entregada en vivo (component current): ',result.registers[0],' s/u')

#5.2.20. Component current BSW hund
result=client.read_holding_registers(6484,2,unit=1)
print('BSW hund en vivo (component current): ',result.registers[0],' s/u')

#5.2.22. Component current API gravity tenths
result=client.read_holding_registers(6676,2,unit=1)
print('Gravidad API en vivo (component current): ',result.registers[0]/10,' s/u')




#Meter k-factor
result=client.read_holding_registers(1770,2,unit=1)
print('Factor k: ',result.registers[0])

#
result=client.read_holding_registers(1970,2,unit=1)
print('Meter factor 1: ',result.registers[0]/10000)

#
result=client.read_holding_registers(1974,2,unit=1)
print('Meter factor 2: ',result.registers[0]/10000)

#
result=client.read_holding_registers(1976,2,unit=1)
print('Meter factor 3: ',result.registers[0]/10000)

#
result=client.read_holding_registers(1980,2,unit=1)
print('Meter factor 4: ',result.registers[0]/10000)


#
result=client.read_holding_registers(1984,2,unit=1)
print('Meter factors used: ',result.registers[0])

client.close()
