from django.shortcuts import render
import requests
# Create your views here.

def get_weather(request):
    weatherdict = {}
    if "location" in request.GET:
        location = request.GET['location']
        url = f'http://api.weatherapi.com/v1/forecast.json?key=581f26cd97c24faa809164418230507%20&q={location}&days=2&aqi=no' 
        unordered = requests.get(url)
        weather = unordered.json()
        weatherdict=weather
        preavgtempF=[]
        print(weatherdict)
    return render(request,'weather.html',{'weatherdict':weatherdict})


'''


subwebsite (ifneeded) >>>

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


iteration (if needed) >>>

for i in weather:
            weather_data = weather(
                location = location,
                temp_c = i['temp_c'],
                temp_f = i['temp_f'],
                wind_mph = i['wind_mph'],
                wind_kph = i['wind_kph'],
                weathertext = i['condition']['text'],
                weatherimage = i['condition']['icon'])

testing forecast averages here >>>

x=weatherdict['forecast']
        for i in x['forecastday']:
            x=0
            while x<24:
                preavgtempF.append(i[f'{x}'].temp_f)
                x+=1
        avgtempF=range(int(preavgtempF))/len(int(preavgtempF))
                '''