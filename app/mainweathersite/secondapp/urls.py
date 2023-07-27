from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #empty path, uses views function called index
    path("<int:location_id>/weather/", views.weather, name="weather") #secondapp/XXXXX/weather
]