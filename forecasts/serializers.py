from rest_framework import serializers
from .models import Forecast

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = [
            'id', 'location', 'forecast_date', 'temperature_min', 'temperature_max',
            'humidity', 'precipitation_probability', 'wind_speed', 'wind_direction', 'created_at'
        ]

    def validate(self, data):
        temperature_min = data.get('temperature_min')
        temperature_max = data.get('temperature_max')

        if temperature_min and temperature_max and temperature_min > temperature_max:
            raise serializers.ValidationError({
                "temperature_min": "Minimal harorat maksimal haroratdan katta bo‘lishi mumkin emas."
            })

        precipitation_probability = data.get('precipitation_probability')
        if precipitation_probability and (precipitation_probability < 0 or precipitation_probability > 100):
            raise serializers.ValidationError({
                "precipitation_probability": "Yog‘ingarchilik ehtimoli 0 dan 100 gacha bo‘lishi kerak."
            })

        wind_direction = data.get('wind_direction')
        if wind_direction and (wind_direction < 0 or wind_direction >= 360):
            raise serializers.ValidationError({
                "wind_direction": "Shamol yo'nalishi 0-359 gradus oralig'ida bo‘lishi kerak."
            })

        return data
