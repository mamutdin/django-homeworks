from django.urls import path

from measurement.views import SensorView, SensorUpdate, MeasurementCreate, SensorDetail

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensor-detail/<int:pk>/', SensorDetail.as_view()),
]
