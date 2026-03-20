import requests
from typing import Optional, Dict

import os
API_KEY = os.getenv('OPENWEATHER_API_KEY', 'd6f3ec3dda9f68c17259ce691fd62aa4')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city: str) -> Optional[Dict]:
    try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'weather': data['weather'][0]['main'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }

            return weather_data
        else:
            return None

    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_features_for_ml(weather_data: Dict) -> Dict:
    return {
        'temperature': weather_data['temperature'],
        'humidity': weather_data['humidity'],
        'pressure': weather_data['pressure'],
        'wind_speed': weather_data['wind_speed']
    }
