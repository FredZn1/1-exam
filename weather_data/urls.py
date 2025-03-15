from django.urls import path
from .views import WeatherDataListCreateAPIView, WeatherDataRetrieveUpdateDestroyAPIView, WeatherDataByLocationAPIView

urlpatterns = [
    path('weather-data/', WeatherDataListCreateAPIView.as_view(), name='weather-data-list-create'),  # GET, POST
    path('weather-data/<int:pk>/', WeatherDataRetrieveUpdateDestroyAPIView.as_view(), name='weather-data-detail'),  # GET, PUT, DELETE
    path('weather-data/location/<int:location_id>/', WeatherDataByLocationAPIView.as_view(), name='weather-data-by-location'),  # GET
]
