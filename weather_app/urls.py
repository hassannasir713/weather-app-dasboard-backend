from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/<str:city>/', views.get_weather, name='get_weather'),
    path('add_favorite/', views.add_favorite_city, name='add_favorite_city'),
    path('search_history/', views.search_history, name='search_history'),
]
