from django.urls import path
from .views import (
    WeatherDataListCreateAPIView,
    WeatherDataRetrieveUpdateDestroyAPIView,
    WeatherDataByLocationAPIView,
    TemperatureAverageAPIView,
    PrecipitationSumAPIView,
    WindSpeedMaxAPIView
)

urlpatterns = [
    path('weather-data/', WeatherDataListCreateAPIView.as_view(), name='weather-data-list-create'),
    path('weather-data/<int:pk>/', WeatherDataRetrieveUpdateDestroyAPIView.as_view(), name='weather-data-detail'),
    path('weather-data/location/<int:location_id>/', WeatherDataByLocationAPIView.as_view(), name='weather-data-by-location'),
    path('weather-data/analytics/temperature-avg/', TemperatureAverageAPIView.as_view(), name='temperature-average'),
    path('weather-data/analytics/precipitation-sum/', PrecipitationSumAPIView.as_view(), name='precipitation-sum'),
    path('weather-data/analytics/wind-speed-max/', WindSpeedMaxAPIView.as_view(), name='wind-speed-max'),
]
