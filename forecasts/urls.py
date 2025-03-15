from django.urls import path
from .views import (
    ForecastListCreateAPIView,
    ForecastRetrieveUpdateDestroyAPIView,
    ForecastByLocationAPIView
)

urlpatterns = [
    path('forecasts/', ForecastListCreateAPIView.as_view(), name='forecasts-list-create'),
    path('forecasts/<int:id>/', ForecastRetrieveUpdateDestroyAPIView.as_view(), name='forecasts-detail'),
    path('forecasts/location/<int:location_id>/', ForecastByLocationAPIView.as_view(), name='forecasts-by-location'),
]
