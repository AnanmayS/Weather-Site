from ast import main
from distutils.log import Log
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import City
import urllib.request
import json
from datetime import datetime
import pytz
from django.contrib.gis.geoip2 import GeoIP2
from ratelimit.decorators import ratelimit



# Create your views here.

def index(request):
    if request.method == "POST":
        try:
            new_city= request.POST.get("city_name")
            newCityobj = City()
            newCityobj.name = new_city
            newCityobj.save()
            currentCity = new_city
            start_url = ('https://api.openweathermap.org/data/2.5/weather?q='+currentCity+'&units=imperial&appid=6c76c712ea6e76177822c9e04f9ef5cc')
            url = start_url.replace(" ", "%20")
            source = urllib.request.urlopen(url).read()
            cityWet = json.loads(source)
            lat = cityWet['coord']['lat']
            Log = cityWet['coord']['lon']
            timeURL = (f'https://timezone.abstractapi.com/v1/current_time/?api_key=91ad59af71fe47609589e9107984c575&location={currentCity}')
            timeNospace = timeURL.replace(" ", "%20")
            timeRead = urllib.request.urlopen(timeNospace).read()
            timeOpen = json.loads(timeRead)
            zone = timeOpen['timezone_location']
            timezone = pytz.timezone(zone)
            now = datetime.now(timezone)
            CurrCity = {
                'cityName': cityWet['name'],
                'temperature': int(cityWet['main']['temp']),
                'text': cityWet['weather'][0]['description'],
                'main': cityWet['weather'][0]['main'],
                'img': cityWet['weather'][0]['icon'],
                'date': now.strftime("%H:%M - %A, %d %b '%y"),
                'wind': int(cityWet['wind']['speed']),
                'humid': int(cityWet['main']['humidity']),
                'cloud': cityWet['clouds']['all'],
                'High': int(cityWet['main']['temp_max']),
                'Low': int(cityWet['main']['temp_min']),
            }
            
            return render(request, 'weatherApp/city.html', CurrCity)
        except:
            getUserip = urllib.request.urlopen('https://ipgeolocation.abstractapi.com/v1/?api_key=c70724edb473444cb4910bbc104fd49c').read()
            openip = json.loads(getUserip)
            ip = openip['ip_address']
            userIP = urllib.request.urlopen(f'http://ip-api.com/json/{ip}').read()
            userIPcheck = json.loads(userIP)
            city = userIPcheck['city']
            start_url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=6c76c712ea6e76177822c9e04f9ef5cc')
            url = start_url.replace(" ", "%20")
            source = urllib.request.urlopen(url).read()
            cityWet = json.loads(source)
            zone = userIPcheck['timezone']
            timezone = pytz.timezone(zone)
            now = datetime.now(timezone) 
            CurrCity = {
                    'cityName': cityWet['name'],
                    'temperature': int(cityWet['main']['temp']),
                    'text': cityWet['weather'][0]['description'],
                    'main': cityWet['weather'][0]['main'],
                    'img': cityWet['weather'][0]['icon'],
                    'date': now.strftime("%H:%M - %A, %d %b '%y"),
                    'wind': int(cityWet['wind']['speed']),
                    'humid': int(cityWet['main']['humidity']),
                    'cloud': cityWet['clouds']['all'],
                    'High': int(cityWet['main']['temp_max']),
                    'Low': int(cityWet['main']['temp_min']),
                }

            return render(request, 'weatherApp/city.html', CurrCity)
    else:
        getUserip = urllib.request.urlopen('https://ipgeolocation.abstractapi.com/v1/?api_key=c70724edb473444cb4910bbc104fd49c').read()
        openip = json.loads(getUserip)
        ip = openip['ip_address']
        userIP = urllib.request.urlopen(f'http://ip-api.com/json/{ip}').read()
        userIPcheck = json.loads(userIP)
        city = userIPcheck['city']
        start_url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=6c76c712ea6e76177822c9e04f9ef5cc')
        url = start_url.replace(" ", "%20")
        source = urllib.request.urlopen(url).read()
        cityWet = json.loads(source)
        zone = userIPcheck['timezone']
        timezone = pytz.timezone(zone)
        now = datetime.now(timezone) 
        CurrCity = {
                'cityName': cityWet['name'],
                'temperature': int(cityWet['main']['temp']),
                'text': cityWet['weather'][0]['description'],
                'main': cityWet['weather'][0]['main'],
                'img': cityWet['weather'][0]['icon'],
                'date': now.strftime("%H:%M - %A, %d %b '%y"),
                'wind': int(cityWet['wind']['speed']),
                'humid': int(cityWet['main']['humidity']),
                'cloud': cityWet['clouds']['all'],
                'High': int(cityWet['main']['temp_max']),
                'Low': int(cityWet['main']['temp_min']),
            }

        return render(request, 'weatherApp/city.html', CurrCity)

def myLocation(request):
    if request.method == "POST":
        getUserip = urllib.request.urlopen('https://ipgeolocation.abstractapi.com/v1/?api_key=c70724edb473444cb4910bbc104fd49c').read()
        openip = json.loads(getUserip)
        ip = openip['ip_address']
        userIP = urllib.request.urlopen(f'http://ip-api.com/json/{ip}').read()
        userIPcheck = json.loads(userIP)
        city = userIPcheck['city']
        start_url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=6c76c712ea6e76177822c9e04f9ef5cc')
        url = start_url.replace(" ", "%20")
        source = urllib.request.urlopen(url).read()
        cityWet = json.loads(source)
        zone = userIPcheck['timezone']
        timezone = pytz.timezone(zone)
        now = datetime.now(timezone)    
        CurrCity = {
            'cityName': cityWet['name'],
            'temperature': int(cityWet['main']['temp']),
            'text': cityWet['weather'][0]['description'],
            'main': cityWet['weather'][0]['main'],
            'img': cityWet['weather'][0]['icon'],
            'date': now.strftime("%H:%M - %A, %d %b '%y"),
            'wind': int(cityWet['wind']['speed']),
            'humid': int(cityWet['main']['humidity']),
            'cloud': cityWet['clouds']['all'],
            'High': int(cityWet['main']['temp_max']),
            'Low': int(cityWet['main']['temp_min']),
        }
        
        return render(request, 'weatherApp/city.html', CurrCity)
    else:
        getUserip = urllib.request.urlopen('https://ipgeolocation.abstractapi.com/v1/?api_key=c70724edb473444cb4910bbc104fd49c').read()
        openip = json.loads(getUserip)
        ip = openip['ip_address']
        userIP = urllib.request.urlopen(f'http://ip-api.com/json/{ip}').read()
        userIPcheck = json.loads(userIP)
        city = userIPcheck['city']
        start_url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&appid=6c76c712ea6e76177822c9e04f9ef5cc')
        url = start_url.replace(" ", "%20")
        source = urllib.request.urlopen(url).read()
        cityWet = json.loads(source)
        zone = userIPcheck['timezone']
        timezone = pytz.timezone(zone)
        now = datetime.now(timezone) 
        CurrCity = {
            'cityName': cityWet['name'],
            'temperature': int(cityWet['main']['temp']),
            'text': cityWet['weather'][0]['description'],
            'main': cityWet['weather'][0]['main'],
            'img': cityWet['weather'][0]['icon'],
            'date': now.strftime("%H:%M - %A, %d %b '%y"),
            'wind': int(cityWet['wind']['speed']),
            'humid': int(cityWet['main']['humidity']),
            'cloud': cityWet['clouds']['all'],
            'High': int(cityWet['main']['temp_max']),
            'Low': int(cityWet['main']['temp_min']),
        }
        
        return render(request, 'weatherApp/city.html', CurrCity)
