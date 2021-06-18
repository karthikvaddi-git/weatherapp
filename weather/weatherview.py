from django.http import HttpResponse
from django.shortcuts import render
import requests


def view(request):
    if request.method == "GET":
        city = 'hyderabad'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=30e89d88a099deaf9c96ca871c1be095'
        data = requests.get(url).json()
        print(data)
        payload = {'city': data['name'], 'weather': data['weather'][0]['main'], 'timezone': data['timezone'],
                   'icon': data['weather'][0]['icon'], 'temperature': int(data['main']['temp'] - 273)}

        context = {"data": payload}

    return render(request, "wheatertemplate.html", context)



def country(request):
    if request.method=="POST":
        city = request.POST['searchcity']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=30e89d88a099deaf9c96ca871c1be095'
        data = requests.get(url).json()
        print(data)
        payload = {'city': data['name'], 'weather': data['weather'][0]['main'], 'timezone': data['timezone'],
                   'icon': data['weather'][0]['icon'], 'temperature': int(data['main']['temp'] - 273)}

        context = {"data": payload}

    if request.method=="GET":


          city = 'hyderabad'
          url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=30e89d88a099deaf9c96ca871c1be095'
          data = requests.get(url).json()
          print(data)
          payload = {'city': data['name'], 'weather': data['weather'][0]['main'], 'timezone': data['timezone'],
                     'icon': data['weather'][0]['icon'], 'temperature': int(data['main']['temp'] - 273)}

          context = {"data": payload}

    return render(request,"wheatertemplate.html",context)




