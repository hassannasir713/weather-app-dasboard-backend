from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import FavoriteCity, SearchHistory
from django.http import JsonResponse
from .consumers import WeatherConsumer


def index(request):
    return render(request, 'index.html')


async def get_weather(request, city):
    weather_consumer = WeatherConsumer()
    weather_data = await weather_consumer.fetch_weather(city)
    if weather_data:
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'Failed to fetch weather data'}, status=400)


@login_required
def add_favorite_city(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        favorite_city = FavoriteCity(user=request.user, city_name=city_name)
        favorite_city.save()
        return redirect('index')
    return render(request, 'add_fav_city.html')


@login_required
def search_history(request):
    search_history = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'search_history.html', {'search_history': search_history})
