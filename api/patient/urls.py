from django.urls import path
from .views import *

urlpatterns = [
    path('paciente/', PacienteViews.as_view()),
    path('paciente/<int:id>', PacienteViews.as_view()),
    path('paciente/<int:id>/incubadora', PacienteIncubadoraViews.as_view()),
]