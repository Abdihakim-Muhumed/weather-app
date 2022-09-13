from multiprocessing import context
from urllib import response
from django.shortcuts import render
import requests
import json
from datetime import datetime
# Create your views here.

def index(request):
    if request.method == 'POST':
        API_KEY = 'cde0a72800580fe756fdf58fb2984965'
        city_name = request.POST.get('city')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'          
        url = "https://api.openweathermap.org/data/2.5/weather?q=Nairobi&appid=cde0a72800580fe756fdf58fb2984965&units=metric"
        response = requests.get(url).json()
        current_time = datetime.now()
        formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
        city_weather_update = {
            'city': city_name,
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
            'temperature': 'Temperature: '+ str(response['main']['temp']) + '°C',
            'country_code': response['sys']['country'],
            'wind': 'Wind: '+ str(response['wind']['speed']) + 'km/h',
            'humidity': 'Humidity: '+str(response['main']['humidity']) + '%',
            'time': formatted_time
                
        }
        
    else:
        city_weather_update = {}

    context = {
        'city_weather_update': city_weather_update
    }
        
    return render(request, 'weatherApp/index.html', context)
    #try:
        # checking for POST method
    
    #except:
    #   return render(request, 'weatherApp/404.html')