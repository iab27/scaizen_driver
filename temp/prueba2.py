#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyowm
from random import randrange

print(randrange(-10,10))

owm = pyowm.OWM('9e3968403ed2adad028a4604ef5e3530')
#obs = owm.weather_at("Estado de Jalisco","MX")
obs = owm.weather_at_coords(20.33333,-103.666672)

print(obs.get_reception_time())