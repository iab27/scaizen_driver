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
client.connect()



#Fecha y hora
timeStamp=client.read_holding_registers(0x0023,12,unit=1)
#5.2.1. Preset quantity in whole units
GOVsolicitado=client.read_holding_registers(4036,2,unit=1)
#5.2.10. Component delivered gross quantity in whole units
GOVcomponente=client.read_holding_registers(4372,2,unit=1)
#5.2.8. Meter delivered gross quantity in whole units
GOVtotal=client.read_holding_registers(4192,2,unit=1)
#5.2.11. Component delivered net quantity in whole units
GSV=client.read_holding_registers(4564,2,unit=1)
#5.2.7. Preset gross flow rate in whole units
flujoPreset=client.read_holding_registers(4180,2,unit=1)
#5.2.9. Meter gross flow rate in whole units
flujoTR=client.read_holding_registers(4312,2,unit=1)
#5.2.13. Component batch average pressure in tenths or hundredths
presionPreset=client.read_holding_registers(4948,2,unit=1)
#5.2.16. Component current pressure in hundredths
presionTR=client.read_holding_registers(4948,2,unit=1)
#5.2.17. Component current density in tenths
densidadTR=client.read_holding_registers(5716,2,unit=1)
#5.2.14. Component batch average density/relative density/gravity
densidadComponent=client.read_holding_registers(5140,2,unit=1)
#5.2.15. Component current temp in hundredths
temperaturaTR=client.read_holding_registers(5332,2,unit=1)
#5.2.4. Preset batch average temp in tenths or hundredths
temperaturaAvg=client.read_holding_registers(4108,2,unit=1)
#5.2.22. Component current mass delivered
masaTR=client.read_holding_registers(6868,2,unit=1)
#5.2.20. Component current BSW hund
BSWTR=client.read_holding_registers(6484,2,unit=1)
#5.2.22. Component current API gravity tenths
gravidadTR=client.read_holding_registers(6676,2,unit=1)
#Meter k-factor
kFactor=client.read_holding_registers(1770,2,unit=1)


#Esto lo modifiqué con mis variables
servidor_driver_ucl = {
    "timestamp": listToString(timeStamp.registers),
    "data": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "config": {
        "version": 0.1,
        "tipo": "driver_ucl_rt",
    },
    "ucl":{
        "config": {
            "version": 0.1,
            "tipo": "ucl",
            "id_instrumentacion": "23",
            "nombre": "UCL 01",
            "producto1": "regular",
            "producto2": "premium"
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_en_espera": False,
            "estado_en_uso": True,
        },
        "data_orden":{
            "id_orden_actual": "23",
            "cantidad_programada": str(GOVsolicitado.registers[0]),
            "cantidad_componente": str(GOVcomponente.registers[0]),
            "cantidad_cargada": str(GOVtotal.registers[0]),
            "cantidad_restante": str(GOVtotal.registers[0]-GOVsolicitado.registers[0]),
            "cantidad_gsv": str(GSV.registers[0]),
            "unidad": "l",
            "producto": "premium"

        }
    },

    "mdp":{
        "config": {
            "version": 0.1,
            "tipo": "mdp",
            "id_instrumentacion": "23",
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_en_espera": False,
            "estado_en_uso": True
        },
        "data": {
            "flujo": str(flujoTR.registers[0]),
            "flujoPreset": str(flujoPreset.registers[0]),
            "unidad": "l/min",
        }
    },
    "rtd":{
        "config": {
            "version": 0.1,
            "tipo": "rtd",
            "id_instrumentacion": "26",
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_sensando": True
        },
        "data": {
            "temperatura": str(temperaturaTR.registers[0]/100),
            "temperaturaAvg": str(temperaturaAvg.registers[0]),
            "unidad": "c",
        }
    },
    "baumanometro":{
        "config": {
            "version": 0.1,
            "tipo": "baumanometro",
            "id_instrumentacion": "36",
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_sensando": True
        },
        "data": {
            "presion": str(presionTR.registers[0]),
            "presionPreset": str(presionPreset.registers[0]),
            "unidad": "kPa",
        }
    },
    "densimetro":{
        "config": {
            "version": 0.1,
            "tipo": "densimetro",
            "id_instrumentacion": "37",
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_sensando": True
        },
        "data": {
            "densidadTR": str(densidadTR.registers[0]),
            "densidadComponent": str(densidadComponent.registers[0]),
            "unidad": "Kg m^3",
        }
    },
    "caudalimetro":{
        "config": {
            "version": 0.1,
            "tipo": "caudalimetro",
            "id_instrumentacion": "38",
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_sensando": True
        },
        "data": {
            "masaTR": str(masaTR.registers[0]),
            "unidad": "s/u",
        }
    },
    "bsw":{
        "config": {
            "version": 0.1,
            "tipo": "bsw",
            "id_instrumentacion": "39",
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_sensando": True
        },
        "data": {
            "BSWTR": str(BSWTR.registers[0]),
            "unidad": "s/u",
        }
    },
    "gravidad":{
        "config": {
            "version": 0.1,
            "tipo": "gravidad",
            "id_instrumentacion": "40",
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_sensando": True
        },
        "data": {
            "gravidadTR": str(gravidadTR.registers[0]),
            "unidad": "s/u",
        }
    },
    "kFactor":{
        "config": {
            "version": 0.1,
            "tipo": "kFactor",
            "id_instrumentacion": "26",
        },
        "servidor": {
            "online": True,
        },
        "online_status": {
            "estado_sensando": True
        },
        "data": {
            "kFactor": str(kFactor.registers[0]),
            "unidad": "adimensional",
        }
    },
    "vcf":{
        "config": {
            "version": 0.1,
            "tipo": "vcf",
            "id_instrumentacion": "12",
        },
        "servidor": {
            "online": True,
        },
        "data": {
            "estado_abierta": False,
        }
    },
    # "vcf_descarga": {
    #     "config": {
    #         "version": 0.1,
    #         "tipo": "vcf",
    #         "id_instrumentacion": "12",
    #     },
    #     "servidor": {
    #         "online": True,
    #     },
    #     "data": {
    #         "estado_abierta": True,
    #     }
    # },
    "valvula_de_tanques":[
        {
            "config": {
                "version": 0.1,
                "tipo": "vcf",
                "id_instrumentacion": "12",
                "producto": "regular"
            },
            "servidor": {
                "online": True,
            },
            "data": {
                "estado_abierta": True,
            }
        },
        {
            "config": {
                "version": 0.1,
                "tipo": "vcf",
                "id": "12",
                "producto": "premium"
            },
            "servidor": {
                "online": True,
            },
            "data": {
                "estado_abierta": True,
            }
        },
        # {
        #     "config": {
        #         "version": 0.1,
        #         "tipo": "vcf",
        #         "id": "12",
        #         "producto": "diesel"
        #     },
        #     "servidor": {
        #         "online": True,
        #     },
        #     "data": {
        #         "estado_abierta": True,
        #     }
        # }
    ],
    "permisivo_tierra":{
        "config": {
            "version": 0.1,
            "tipo": "permisivo",
            "id_instrumentacion": "12",
        },
        "servidor": {
            "online": True,
        },
        "data": {
            "estado_activado": True,
        }
    },
    "permisivo_sobrellenado":{
        "config": {
            "version": 0.1,
            "tipo": "permisivo",
            "id_instrumentacion": "12",
        },
        "servidor": {
            "online": True,
        },
        "data": {
            "estado_activado": True,
        }
    }
}

logging.info(servidor_driver_ucl)
json_txt = json.dumps( servidor_driver_ucl)


tarea_id = administracion_de_tareas.nueva_tarea_ucl_rt(json_txt)


client.close()


#Esto es lo único que comenté
#with open('json.txt', 'w') as fp:
#    json.dump(servidor_driver_ucl, fp)
