from flask import Flask, render_template
from datetime import datetime
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import time
import pytemperature


app = Flask(__name__)

@app.route("/")
def hello():

    time = datetime.now().strftime('%H:%M') #times
    date = datetime.now().strftime('%m - %d') #times



    with open('soccerPost.txt') as f:
        content = [line.decode('utf-8').strip() for line in f.readlines()] #get txt file headlines soccer
    with open('wnPost.txt') as f1:
        content1 = [line.decode('utf-8').strip() for line in f1.readlines()] #get txt file healines world news

    request = ('http://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=9b56b06ab4c7f06821ccf55e3e10fce5')

    response = urllib2.urlopen(request)
    str_response = response.read().decode('utf-8')
    obj = json.loads(str_response)

    # TempLow Kelvin
    tempLow_kelvin = obj['main']['temp_min']
    tempHigh_kelvin = obj['main']['temp_max']
    tempCur_kelvin = obj['main']['temp']

    # TempHigh Farenheit
    tempLow_faren = pytemperature.k2f(tempLow_kelvin)
    tempHigh_faren = pytemperature.k2f(tempHigh_kelvin)
    tempCur_faren = pytemperature.k2f(tempCur_kelvin)

    # Weather Description
    descrip = obj['weather'].pop()
    descrip = descrip.values()[3]

    return render_template("index.html", time=time, date=date, content=content, content1=content1, tempHigh_faren=tempHigh_faren,
                           tempLow_faren=tempLow_faren, tempCur_faren=tempCur_faren, descrip=descrip)

if __name__ == "__main__":
    app.run()

