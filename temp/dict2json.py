#!/usr/bin/env python

import logging
import json
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)


servidor_driver_ucl = {
    "timestamp": "2020-01-23 16:30:58",
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
            "estado_en_uso": False,
        },
        "data_orden":{
            "id_orden_actual": "23",
            "cantidad_programada": 15000,
            "cantidad_cargada": 12000,
            "cantidad_restante": 3000,
            "unidad": "l",
            "producto": "regular"

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
            "flujo": 3000,
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
            "temperatura": 23.45,
            "unidad": "c",
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
            "estado_abierta": True,
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
json_txt = json.dumps(servidor_driver_ucl)

with open('json.txt', 'w') as fp:
    json.dump(servidor_driver_ucl, fp)
