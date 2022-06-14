from django.urls import path
from .views import *

urlpatterns = [
    path('sensor/', SensorViews.as_view()),
    path('sensor/<int:id>', SensorViews.as_view()),
    path('alarma/', AlarmaViews.as_view()),
    path('alarma/<int:id>', AlarmaViews.as_view()),
    path('topic/', TopicViews.as_view()),
    path('topic/<int:id>', TopicViews.as_view()),
    path('sensor/<int:id>/alarma', SensorAlarmaViews.as_view()),
]