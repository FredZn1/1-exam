from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Avg, Sum, Max
from .models import WeatherData
from .serializers import WeatherDataSerializer

class WeatherDataListCreateAPIView(mixins.ListModelMixin,
                                   mixins.CreateModelMixin,
                                   generics.GenericAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class WeatherDataRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                              mixins.UpdateModelMixin,
                                              mixins.DestroyModelMixin,
                                              generics.GenericAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class WeatherDataByLocationAPIView(APIView):
    def get(self, request, location_id):
        weather_data = WeatherData.objects.filter(location_id=location_id)
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)

class TemperatureAverageAPIView(APIView):
    def get(self, request):
        result = WeatherData.objects.aggregate(avg_temp=Avg('temperature'))
        avg_temp = result['avg_temp']
        return Response({"average_temperature": avg_temp})

class PrecipitationSumAPIView(APIView):
    def get(self, request):
        result = WeatherData.objects.aggregate(total_precip=Sum('precipitation'))
        total_precip = result['total_precip']
        return Response({"total_precipitation": total_precip})

class WindSpeedMaxAPIView(APIView):
    def get(self, request):
        result = WeatherData.objects.aggregate(max_speed=Max('wind_speed'))
        max_speed = result['max_speed']
        return Response({"max_wind_speed": max_speed})
