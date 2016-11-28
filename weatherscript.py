import requests
from weather.map.models import Weather
from weather.map.models import Region

def getweather(reg, latitude, longitude): #reg is the region
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat='+str(latitude)+'&lon='+str(longitude))
    q = Weather(region = reg, temperature = r.json()["main"]["temp"])
    q.save()

