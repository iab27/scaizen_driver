#!/usr/bin/env python

#Esto lo agregué
from pymodbus.client.sync import ModbusTcpClient
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests
import administracion_de_tareas
import time	 
import sys
#import broker

from tornado.websocket import websocket_connect
import asyncio
import json
#import msvcrt

#Para simular
from datetime import datetime
from random import randrange

#Esto no lo modifiqué
import logging
import json
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)

#from asyncproc import ProcessManager

#manager = ProcessManager()

#Esto es para SIMULAR
simulation = 1; #1 para simular y 0 para no
#Modificar por el USUARIO
ventana = 2         #Minutos (configurado por el cliente)
GOVsolicitado = 500 #Litros (seleccionado por el cliente)
flujoPreset = 1500  #Litros por minuto (depende del medidor)
tiempoMuestreo = 30 #Segundos en que se solicitará info a la UCL
tipoProducto = 1    #1 para premium y 0 para regular
if (tipoProducto == 1):
    producto="premium"
else:
    producto="regular"
#No modificar por el USUARIO
GOVcomponente = 0   #Inicio de lo surtido
factor = 0.98
kFactor = 19
temperatura = 27
GOVtotal = 0


#Para el envio de datos
API_ENDPOINT="http://127.0.0.1:5510/endpointdata"
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
    return ("{0:04.2f}".format(float(n) ) ).zfill(7)

def formato_temperatura(n):
    return ("{0:02.2f}".format( float(n) )).zfill(5)


async def main():
    if simulation==1:
        
        if ((GOVtotal+27)<(GOVsolicitado)): 
            timeStamp = datetime.now()
            print(timeStamp)
            minutoActual=timeStamp.minute
            if 'minutoPasado' in locals():
                print(minutoActual)
                print(minutoPasado)
                if (minutoActual-minutoPasado >= ventana):
                    print('almacenar')
                    minutoPasado=minutoActual
                else:
                    print('no almacenar')
            else:
                print('inicio almacenar')
                minutoPasado=minutoActual

            flujoTR = flujoPreset + randrange(-3,3)
            GOVcomponente = GOVcomponente + flujoTR*(tiempoMuestreo/60)
            GOVtotal = GOVcomponente
            GSV = GOVtotal * factor
            time.sleep(tiempoMuestreo)

            
            #Esto lo modifiqué con mis variables
            servidor_driver_ucl = {
                "timestamp": listToString(timeStamp),
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
                        "cantidad_programada": str(GOVsolicitado),
                        "cantidad_componente": str(GOVcomponente),
                        "cantidad_cargada": str(GOVtotal),
                        "cantidad_restante": str(GOVtotal-GOVsolicitado),
                        "cantidad_gsv": str(GSV),
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
                        "flujo": formato_flujo(str(flujoTR.registers[0])),
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
                        "temperatura": formato_temperatura(str((temperaturaTRrgl.registers[0]/100)+(temperaturaTRprm.registers[0]/100))),
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

            json_txt = json.dumps( servidor_driver_ucl)

            print(json_txt)

            await conn.write_message(json_txt)

            await asyncio.sleep(0.5)
    else:
        try:
            conn = await websocket_connect(url)
            client=ModbusTcpClient('192.168.0.200')
            #client.connect()

            while 1:
                """
                if client.connect():
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
                    temperaturaTRrgl=client.read_holding_registers(5332,2,unit=1)
                    temperaturaTRprm=client.read_holding_registers(5334,2,unit=1)
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
                """


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
                temperaturaTRrgl=client.read_holding_registers(5332,2,unit=1)
                temperaturaTRprm=client.read_holding_registers(5334,2,unit=1)
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

                if temperaturaTRprm.registers[0]!=0:
                    producto="premium"
                else:
                    producto="regular"


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
                            "flujo": formato_flujo(str(flujoTR.registers[0])),
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
                            "temperatura": formato_temperatura(str((temperaturaTRrgl.registers[0]/100)+(temperaturaTRprm.registers[0]/100))),
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