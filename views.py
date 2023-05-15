import requests
import logging
from django.http import JsonResponse
from rest_framework.decorators import api_view
from cacheops import cached
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

CACHE_TTL = 300 # 5 minutes

@api_view(['GET'])
@cached(timeout=CACHE_TTL)
def current_weather(request):
    city = request.GET.get('city')
    if not city:
        return JsonResponse({'error': 'City parameter is required'}, status=400)
    
    api_key = 'f3ed51b69a289e802be8af96e841cb18'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'city': data['name'],
            'country': data['sys']['country']
        }
        return JsonResponse({'weather': weather})
    else:
        logger.error(f"Request failed with status code {response.status_code}")
        return JsonResponse({'error': 'Invalid city or API error'}, status=400)

@api_view(['GET'])
@cached(timeout=CACHE_TTL)
def forecast_weather(request):
    city = request.GET.get('city')
    if not city:
        return JsonResponse({'error': 'City parameter is required'}, status=400)
    
    api_key = 'f3ed51b69a289e802be8af96e841cb18'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        forecasts = []
        for item in data['list']:
            forecast = {
                'date': item['dt_txt'],
                'description': item['weather'][0]['description'],
                'temperature': item['main']['temp'],
                'humidity': item['main']['humidity'],
                'wind_speed': item['wind']['speed'],
                'city': data['city']['name'],
                'country': data['city']['country']
            }
            forecasts.append(forecast)
        return JsonResponse({'forecasts': forecasts})
    else:
        logger.error(f"Request failed with status code {response.status_code}")
        return JsonResponse({'error': 'Invalid city or API error'}, status=400)

@api_view(['GET'])
@cached(timeout=CACHE_TTL)
def past_weather(request):
    city = request.GET.get('city')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if not city:
        return JsonResponse({'error': 'City parameter is required'}, status=400)
    if not start_date or not end_date:
        return JsonResponse({'error': 'Start and end dates are required'}, status=400)
    
    api_key = 'f3ed51b69a289e802be8af96e841cb18'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        past_weather = []
        for item in data['list']:
            if start_date <= item['dt_txt'] <= end_date:
                weather = {
                    'date': item['dt_txt'],
                    'description': item['weather'][0]['description'],
                    'temperature': item['main']['temp'],
                    'humidity': item['main']['humidity'],
                    'wind_speed': item
                }