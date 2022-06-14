from django.urls import path
from .views import *

urlpatterns = [
    path('camara/', CamaraViews.as_view()),
    path('camara/<int:id>', CamaraViews.as_view()),
    path('video/', VideoViews.as_view()),
    path('video/<int:id>', VideoViews.as_view()),
]