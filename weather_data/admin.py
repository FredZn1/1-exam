from django.contrib import admin
from .models import WeatherData

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'temperature', 'humidity', 'pressure', 'wind_speed', 'recorded_at')
    list_filter = ('location', 'recorded_at')
    search_fields = ('location__name',)
    ordering = ('-recorded_at',)
