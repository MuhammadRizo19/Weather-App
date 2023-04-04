from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required


def index(request):
    url = 'http://api.weatherapi.com/v1/current.json?key=46a1a269bdf6459eab3170525233103&q=Tashkent&aqi=yes'

    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json()
    #print(city_weather)
    country = {
        "location":city_weather['location']['name'],
        "w   ind":city_weather['current']["wind_kph"]
    }
    context = {'country':country}
    return render(request, 'index.html', context) 