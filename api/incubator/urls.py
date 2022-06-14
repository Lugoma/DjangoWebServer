from django.urls import path
from .views import *

urlpatterns = [
    path('incubadora/', IncubadoraViews.as_view()),
    path('incubadora/<int:id>', IncubadoraViews.as_view()),
    path('incubadora/<int:id>/sensor', IncubadoraSensorViews.as_view()),
    path('incubadora/<int:id>/sensor_activo', IncubadoraSensorActivoViews.as_view()),
    path('incubadora/<int:id>/camara', IncubadoraCamaraViews.as_view()),
    path('incubadora_activa', IncubadoraActivaViews.as_view()),
    path('incubadora/<int:id>/paciente', IncubadoraPacienteViews.as_view()),
]