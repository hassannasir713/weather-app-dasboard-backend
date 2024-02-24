import json
from channels.generic.websocket import AsyncWebsocketConsumer
import aiohttp
from config import settings


class WeatherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        city = data.get('city')
        if city:
            weather_data = await self.fetch_weather(city)
            await self.send(text_data=json.dumps(weather_data))

    async def fetch_weather(self, city):
        api_key = settings.WEATHERMAP_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    weather_data = {
                        'city': city,
                        'temperature': data['main']['temp'],
                        'humidity': data['main']['humidity'],
                        'wind_speed': data['wind']['speed'],
                        'weather_conditions': data['weather'][0]['description']
                    }
                    return weather_data
                else:
                    return {'error': 'Failed to fetch weather data'}
