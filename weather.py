#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyowm
import json

key = 'OPENWEATHERMAP_API_KEY' #insert your OpenWeatherMap API Key here
location = 'LOCATION' # enter location here, ie. "New York, NY, USA"
temp_scale = 'fahrenheit' # can be changed to 'celsius'
temp_symbol = (u"\u2109").encode('utf-8', 'ignore') # change to unicode 2103 if celsius

condition = ['Snow', 'Sun', 'Rain', 'Cloud', 'Storm', 'Fog']
icon = ['', '', '', '', '', '']

owm = pyowm.OWM(key)

try:
    weather = owm.weather_at_place(location).get_weather()
    
except Exception, e:
    print "Weather N/A"
    exit(0)

temp = str(json.loads(json.dumps(weather.get_temperature(temp_scale)))['temp']) + temp_symbol
status = str(weather.get_status())

successful = False

for i in range(len(condition)):
    if condition[i] in status:
        print icon[i] + ' ' + temp
        successful = True
        break

# defaulting to a cloud icon if no description matches
if not successful:
    print icon[3] + ' ' + temp
