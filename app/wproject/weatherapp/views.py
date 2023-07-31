from django.shortcuts import render
import requests
from weatherapp.models import weatherclass
# Create your views here.

def get_weather(request):
    weatherdict = {}
    all_weather = weatherclass.objects.all().order_by('-id')
    if "location" in request.GET:
        location = request.args.GET['location']
        url = 'http://api.weatherapi.com/v1/current.json?key=581f26cd97c24faa809164418230507%20&q=%s&aqi=no' % location
        unordered = requests.get(url)
        weatherdict = unordered.json()
    return render(request,'weather.html',{'weatherdict':weatherdict})

def weather_detail(request,id):
    try:
        current_weather = weatherclass.objects.get(id = id)
        print(current_weather)
    except weatherclass.DoesNotExist:
        current_weather = None
    return render (
        request,
        'weather_detail.html',
        {'current_weather':current_weather}
    )
'''

for i in weather:
            weather_data = weather(
                location = location,
                temp_c = i['temp_c'],
                temp_f = i['temp_f'],
                wind_mph = i['wind_mph'],
                wind_kph = i['wind_kph'],
                weathertext = i['condition']['text'],
                weatherimage = i['condition']['icon'])
'''