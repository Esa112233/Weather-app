from django.shortcuts import render
from weatherApp.models import WeatherInfoRequired as WI
import requests
from django.http import JsonResponse

# Create your views here.
def weather(request):
    print("hi")
    r = requests.get("http://10.30.42.10:8080/SAFEROneDAQ/data/latestMetAverages?metStationId=1530", auth=('user', 'pass'))
    # print(r.json()[0].get("metData").get("feelsLike"))
    r = r.json()[0].get("metData")
    metStationName = r.get("maxWindSpeed")
    feelsLike = round(r.get("feelsLike") - 273.15, 2)
    temperature = round(r.get("temperature") - 273.15, 2)
    humidity = round(100*r.get("humidity"), 2)
    pressure = round(101.325*r.get("pressure"), 2)
    rainfall = round(100*r.get("rainfall"), 2)
    solarRadiation = round(r.get("solarRadiation"), 2)
    rainRate = round(r.get("rainRate"), 2)
    hStability = r.get("hStability")
    vStability = r.get("vStability")
    windSpeed = round(3.6*r.get("windSpeed"), 2)
    print(rainRate)
    weatherData = WI(
        feelsLike=feelsLike,
        temperature=temperature,
        humidity=humidity,
        pressure=pressure,
        rainfall=rainfall,
        solarRadiation=solarRadiation,
        rainRate=rainRate, hStability=hStability, vStability=vStability)
    weatherData.save()
    try:
        stability = round(r.get("hStability")/r.get("vStability"), 2) # May sometimes be None/None
        return JsonResponse({"feelsLike": feelsLike, "temperature": temperature,
                                                    "humidity": humidity, "pressure": pressure, "rainfall": rainfall, "solarRadiation": solarRadiation,
                                                    "stability": stability, "maxSpeed": windSpeed, "rainRate": rainRate})
    except:
        return JsonResponse({"feelsLike": feelsLike, "temperature": temperature,
                                                    "humidity": humidity, "pressure": pressure, "rainfall": rainfall, "solarRadiation": solarRadiation,
                                                    "stability": None, "rainRate": rainRate, "maxSpeed": windSpeed})
    
    
    
def page(request):
    
    return render(request, "weatherApp/base.html" )