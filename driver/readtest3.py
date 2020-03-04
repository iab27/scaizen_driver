#!/usr/bin/env python

#Esto lo agregué
from pymodbus.client.sync import ModbusTcpClient
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
import administracion_de_tareas
import time	 

#import msvcrt

#Esto no lo modifiqué
import logging
import json
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)


#Esto lo agregué
API_ENDPOINT="http://127.0.0.1:5510/endpointdata"
def listToString(s):
    str1=''
    i=0
    for ele in s:
        if i<1: str1+=chr(ele)
        elif i<2:  str1+=chr(ele)+'-'
        elif i<3:  str1+=chr(ele)
        elif i<4:  str1+=chr(ele)+'-'
        elif i<5:  str1+=chr(ele)
        elif i<6:  str1+=chr(ele)+' '
        elif i<7:  str1+=chr(ele)
        elif i<8:  str1+=chr(ele)+':'
        elif i<9:  str1+=chr(ele)
        elif i<10: str1+=chr(ele)+':'
        else:      str1+=chr(ele)
        i=i+1
    return str1
#logging.basicConfig()
#log=logging.getLogger()
client=ModbusTcpClient('192.168.0.200')

while 1:
    if client.connect():
        #timeStamp
        try:
            timeStamp=client.read_holding_registers(0x0023,12,unit=1)
        except:
            timeStamp.registers[0]=0
        #5.2.1. Preset quantity in whole units
        try:
            GOVsolicitado=client.read_holding_registers(4036,2,unit=1)
        #5.2.10. Component delivered gross quantity in whole units
        try:
            GOVcomponente=client.read_holding_registers(4372,2,unit=1)
        #5.2.8. Meter delivered gross quantity in whole units
        try:
            GOVtotal=client.read_holding_registers(4192,2,unit=1)
        #5.2.11. Component delivered net quantity in whole units
        try:
            GSV=client.read_holding_registers(4564,2,unit=1)
        #5.2.7. Preset gross flow rate in whole units
        try:
            flujoPreset=client.read_holding_registers(4180,2,unit=1)
        #5.2.9. Meter gross flow rate in whole units
        try:
            flujoTR=client.read_holding_registers(4312,2,unit=1)
        #5.2.13. Component batch average pressure in tenths or hundredths
        try:
            presionPreset=client.read_holding_registers(4948,2,unit=1)
        #5.2.16. Component current pressure in hundredths
        try:
            presionTR=client.read_holding_registers(4948,2,unit=1)
        #5.2.17. Component current density in tenths
        try:
            densidadTR=client.read_holding_registers(5716,2,unit=1)
        #5.2.14. Component batch average density/relative density/gravity
        try:
            densidadComponent=client.read_holding_registers(5140,2,unit=1)
        #5.2.15. Component current temp in hundredths
        try:
            temperaturaTRrgl=client.read_holding_registers(5332,2,unit=1)
        try:
            temperaturaTRprm=client.read_holding_registers(5334,2,unit=1)
        #5.2.4. Preset batch average temp in tenths or hundredths
        try:
            temperaturaAvg=client.read_holding_registers(4108,2,unit=1)
        #5.2.22. Component current mass delivered
        try:
            masaTR=client.read_holding_registers(6868,2,unit=1)
        #5.2.20. Component current BSW hund
        BSWTR=client.read_holding_registers(6484,2,unit=1)
        #5.2.22. Component current API gravity tenths
        gravidadTR=client.read_holding_registers(6676,2,unit=1)
        #Meter k-factor
        kFactor=client.read_holding_registers(1770,2,unit=1)

        if temperaturaTRprm.registers[0]!=0:
            producto="premium"
        else:
            producto="regular"
    else:
        timeStamp.registers[0]=[0,0]
        GOVsolicitado.registers[0]=0
        GOVcomponente.registers[0]=0
        GOVtotal.registers[0]=0
        GSV.registers[0]=0
        flujoPreset.registers[0]=0
        flujoTR.registers[0]=0
        presionPreset.registers[0]=0
        presionTR.registers[0]=0
        densidadTR.registers[0]=0
        densidadComponent.registers[0]=0
        temperaturaTRrgl.registers[0]=0
        temperaturaTRprm.registers[0]=0
        temperaturaAvg.registers[0]=0
        masaTR.registers[0]=0
        BSWTR.registers[0]=0
        gravidadTR.registers[0]=0
        kFactor.registers[0]=0
        producto="regular"  
    