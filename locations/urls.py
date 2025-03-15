from django.urls import path
from .views import LocationListCreateAPIView, LocationRetrieveUpdateDestroyAPIView



urlpatterns = [
    path('locations/', LocationListCreateAPIView.as_view(), name='locations-list-create'),
    path('locations/<int:pk>/', LocationRetrieveUpdateDestroyAPIView.as_view(),name='locations-detail')
]