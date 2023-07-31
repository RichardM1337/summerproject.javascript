from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("weather/<int:id>",views.get_weather,name="weather"),
    path('',views.get_weather, name="weather")
]