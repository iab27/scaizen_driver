#!/usr/bin/env python

#Esto lo agregué
from pymodbus.client.sync import ModbusTcpClient
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
import administracion_de_tareas
import time	 
#import broker

from tornado.websocket import websocket_connect
import asyncio
import json

#import msvcrt

#Esto no lo modifiqué
import logging
import sys
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)

#from asyncproc import ProcessManager

#manager = ProcessManager()


from datetime import datetime
from random import randrange
import time


#Esto lo agregué
#API_ENDPOINT="http://127.0.0.1:5510/endpointdata"
API_ENDPOINT="http://127.0.0.1:5510/endpointdata"
#url = "ws://localhost:5500/patin"
url = "ws://localhost:5500/patin"
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

def formato_flujo(n):
    return ("{0:00.0f}".format(float(n) ) ).zfill(1)

def formato_temperatura(n):
    return ("{0:02.2f}".format( float(n) )).zfill(5)


async def main():
    #Modificar por el USUARIO
    simulacion = 1      #Si es , simula, sino, no
    ventana = 2         #Minutos (configurado por el cliente)
    GOVsolicitado = 5000#Litros (seleccionado por el cliente)
    flujoPreset = 770   #Litros por minuto (depende del medidor)
    tiempoMuestreo = 1  #Segundos en que se solicitará info a la UCL
    tipoProducto = 1    #1 para premium y 0 para regular
    if (tipoProducto == 1):
        producto="premium"
    else:
        producto="regular"

    #No modificar
    GOVcomponente = 0   #Inicio de lo surtido
    GOVtotal = 0
    factor = 0.98
    kFactor = 19
    temperatura = 27
    gravidadTR = 0
    BSWTR = 0
    masaTR = 0
    densidadTR = 0
    densidadComponent = 0
    presionPreset = 0
    presionTR = 0
    temperaturaAvg = temperatura
    temperaturaTRrgl = temperatura
    temperaturaTRrpm = temperatura
    flujoTR = flujoPreset


    try:
        conn = await websocket_connect(url)
        #client=ModbusTcpClient('192.168.0.200')
        #client.connect()

        while 1:
            if (((GOVtotal-GOVsolicitado)<=randrange(-27,27)) and (simulacion==1)):
                timeStamp = datetime.now()
                print(timeStamp)
                minutoActual=timeStamp.minute
                if 'minutoPasado' in locals():
                    print(minutoActual)
                    print(minutoPasado)
                    if (minutoActual-minutoPasado >= ventana):
                        print('almacenar*****************************----------------')
                        minutoPasado=minutoActual
                    else:
                        print('no almacenar')
                else:
                    print('inicio almacenar')
                    minutoPasado=minutoActual

                flujoTR = flujoPreset + randrange(-3,3)
                GOVcomponente = GOVcomponente + flujoTR*(tiempoMuestreo/60)
                GOVtotal = GOVcomponente
                GSV = GOVtotal*factor
                time.sleep(tiempoMuestreo)

                #Esto lo modifiqué con mis variables
                servidor_driver_ucl={
                    "timestamp": str(timeStamp),
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
                            "cantidad_programada": str(int(round((GOVsolicitado),0))),
                            "cantidad_componente": str(int(round((GOVcomponente),0))),
                            "cantidad_cargada": str(int(round((GOVtotal),0))),
                            "cantidad_restante": str(int(round((GOVsolicitado-GOVtotal),0))),
                            "cantidad_gsv": str(int(round((GSV),0))),
                            "unidad": "l",
                            "producto": producto

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
                            "flujo": formato_flujo(str(flujoTR)),
                            "flujoPreset": str(flujoPreset),
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
                            "temperatura": formato_temperatura(str((temperatura))),
                            "temperaturaAvg": formato_temperatura(str(temperaturaAvg)),
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
                            "presion": str(presionTR),
                            "presionPreset": str(presionPreset),
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
                            "densidadTR": str(densidadTR),
                            "densidadComponent": str(densidadComponent),
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
                            "masaTR": str(masaTR),
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
                            "BSWTR": str(BSWTR),
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
                            "gravidadTR": str(gravidadTR),
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
                            "kFactor": str(kFactor),
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

                json_txt = json.dumps( servidor_driver_ucl)
                print(json_txt)
            else:
                print('Esperando...')
                simulacion = 0
                time.sleep(20)
   
            json_txt = json.dumps( servidor_driver_ucl)

            await conn.write_message(json_txt)

            await asyncio.sleep(0.5)

        client.close()


        
        
    except ConnectionRefusedError:
        print('error: ConnectionRefusedError')
        sys.exit(1)
    except TimeoutError:
        print('error: TimeoutError')
        sys.exit(1)
    print('done')
    sys.exit(0)

asyncio.run(main())