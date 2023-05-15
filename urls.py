from django.urls import path
from . import views

urlpatterns = [
    path('current/', views.current_weather, name='current_weather'),
    path('past/', views.past_weather, name='past_weather'),
    path('forecast/', views.forecast_weather, name='forecast_weather'),
]
