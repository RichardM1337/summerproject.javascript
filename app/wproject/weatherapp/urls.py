from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("weather/<int:id>",views.weather_detail,name="weather_detail"),
    path('',views.get_weather, name="weather")
]