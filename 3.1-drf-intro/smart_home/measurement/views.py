# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView, \
    ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, \
    MeasurementViewSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreate(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementViewSerializer


class SensorDetail(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
