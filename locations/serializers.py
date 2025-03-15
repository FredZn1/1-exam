from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name", "latitude", "longitude", "elevation", "created_at"]

    def validate(self, data):
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        elevation = data.get("elevation")
        name = data.get("name")

        if latitude is not None and (latitude < -90 or latitude > 90):
            raise serializers.ValidationError({"latitude": "Latitude -90 va 90 orasida bo‘lishi kerak."})

        if longitude is not None and (longitude < -180 or longitude > 180):
            raise serializers.ValidationError({"longitude": "Longitude -180 va 180 orasida bo‘lishi kerak."})

        if elevation is not None and elevation < 0:
            raise serializers.ValidationError({"elevation": "Balandlik manfiy bo‘lishi mumkin emas."})

        if name and Location.objects.filter(name=name).exists():
            raise serializers.ValidationError({"name": "Bu nom bilan joylashuv allaqachon mavjud."})

        return data
