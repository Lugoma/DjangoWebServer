from django.urls import path
from .views import *

urlpatterns = [
    path('camara/', CamaraViews.as_view()),
    path('camara/<int:id>', CamaraViews.as_view()),
]