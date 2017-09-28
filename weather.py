try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import time
import pytemperature

request = ('http://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=9b56b06ab4c7f06821ccf55e3e10fce5')

response = urllib2.urlopen(request)
str_response = response.read().decode('utf-8')
obj = json.loads(str_response)

# TempLow Kelvin
tempLow_kelvin = obj['main']['temp_min']
tempHigh_kelvin = obj['main']['temp_max']
tempCur_kelvin = obj['main']['temp']

# TempHigh Farenheit
tempLow_faren= pytemperature.k2f(tempLow_kelvin)
tempHigh_faren = pytemperature.k2f(tempHigh_kelvin)
tempCur_faren = pytemperature.k2f(tempCur_kelvin)

# Weather Description
descrip = obj['weather'].pop()
descrip = descrip.values()[3]


print tempLow_faren, tempHigh_faren,
