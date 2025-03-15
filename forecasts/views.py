from rest_framework import generics, mixins
from .models import Forecast
from .serializers import ForecastSerializer

class ForecastListCreateAPIView(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                generics.GenericAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ForecastRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                           mixins.UpdateModelMixin,
                                           mixins.DestroyModelMixin,
                                           generics.GenericAPIView):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ForecastByLocationAPIView(generics.ListAPIView):
    serializer_class = ForecastSerializer

    def get_queryset(self):
        location_id = self.kwargs.get('location_id')
        return Forecast.objects.filter(location_id=location_id)
