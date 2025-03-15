from rest_framework import serializers
from .models import WeatherData

class  WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = [
            'id', 'location', 'temperature', 'humidity', 'pressure',
            'wind_speed', 'wind_direction', 'precipitation', 'recorded_at'
        ]

    def validate(self, data):

        if data['temperature'] < -100 or data['temperature'] > 100:
            raise serializers.ValidationError({'temperature': "Harorat -100 dan 100 gacha bo‘lishi kerak."})

        if data['humidity'] < 0 or data['humidity'] > 100:
            raise serializers.ValidationError({'humidity': "Namlik 0% dan 100% gacha bo‘lishi kerak."})

        if data['pressure'] < 800 or data['pressure'] > 1100:
            raise serializers.ValidationError({'pressure': "Bosim 800 hPa dan 1100 hPa gacha bo‘lishi kerak."})

        if data['wind_speed'] < 0:
            raise serializers.ValidationError({'wind_speed': "Shamol tezligi manfiy bo‘lishi mumkin emas."})

        if data['wind_direction'] < 0 or data['wind_direction'] > 360:
            raise serializers.ValidationError({'wind_direction': "Shamol yo‘nalishi 0-360 gradus oralig‘ida bo‘lishi kerak."})

        if data['precipitation'] < 0:
            raise serializers.ValidationError({'precipitation': "Yog‘ingarchilik miqdori manfiy bo‘lishi mumkin emas."})

        return data
