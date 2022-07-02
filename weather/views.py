from django.shortcuts import render
from django.http import JsonResponse
# the HttpResponse module allows you to return stuff without a template  
import requests 
import os
from dotenv import load_dotenv
from .models import Weather
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WeatherSerializer
from weather import serializers


weather_key = os.environ.get('WEATHER_KEY')

# Create your views here.
def get_weather(request): 

  url = f'http://api.weatherapi.com/v1/forecast.json?q=Detroit&key={weather_key}'
  response = requests.get(url)
  data = response.json()
  loc = data['location']['name']
  temp = data['current']['temp_f']
  result = f'{loc}: {temp}'

  newWeatherInstance = Weather(
    created_at = date.today(),
    location = loc,
    temperature = temp
  )

  json_weather_instance = {
    'created_at': date.today(),
    'location': loc,
    'temperature': temp,
  }
  print(newWeatherInstance.location)
  print(newWeatherInstance.created_at)
  print(newWeatherInstance.temperature)
  # perhaps need to use serializers to add to db 

  return JsonResponse(json_weather_instance)

@api_view(['GET'])
def weather_list(request): 
  weathers = Weather.objects.all()
  serializer = WeatherSerializer(weathers, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def weather_detail(request, pk): 
  weathers = Weather.objects.get(id=pk)
  serializer = WeatherSerializer(weathers, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def weather_create(request): 
  serializer = WeatherSerializer(data=request.data)
  # if serializer is valid, send to db 
  if serializer.is_valid(): 
    serializer.save()
  return Response(serializer.data)


@api_view(['GET'])
def make_api_call_and_weather_create(request, query): 
  url = f'http://api.weatherapi.com/v1/forecast.json?q={query}&key={weather_key}'
  response = requests.get(url)
  data = response.json()
  loc = data['location']['name']
  temp = data['current']['temp_f']

  json_weather_instance = {
    'created_at': date.today(),
    'location': loc,
    'temperature': temp,
  }

  serializer = WeatherSerializer(data=json_weather_instance)
  # if serializer is valid, send to db 
  if serializer.is_valid(): 
    serializer.save()
  return Response(serializer.data)


@api_view(['POST'])
def weather_update(request, pk): 
  weather = Weather.objects.get(id=pk)
  serializer = WeatherSerializer(instance=weather, data=request.data)

  if serializer.is_valid(): 
    serializer.save()
  
  return Response(serializer.data)

@api_view(['DELETE'])
def weather_delete(request, pk): 
  weather = Weather.objects.get(id=pk)
  weather.delete()
  
  return Response('item deleted')