from django.shortcuts import render
from django.contrib import messages

import requests

from .models import City
from .forms import CityForm


def index(request):

    cities = City.objects.all()  # return all the cities in the database

    # Change units to units=imperial to display the temperature
    # in degrees Fahrenheit
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST':  # Only true if form is submitted

        # Add actual request data to form for processing
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # print(form.errors)
            messages.add_message(request, messages.ERROR,
                                 'This city already exists.')
        # errors = form.errors

    form = CityForm()
    weather_data = []

    for city in cities:

        # request the API data and convert the JSON to Python data types
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        # add the data for the current city into our list
        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)
