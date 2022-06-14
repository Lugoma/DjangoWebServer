from django.urls import path
from .views import *
from .incubator.urls import urlpatterns as incubator_urls
from .sensor.urls import urlpatterns as sensor_urls
from .camera.urls import urlpatterns as camera_urls
from .patient.urls import urlpatterns as patient_urls

urlpatterns = []

urlpatterns += incubator_urls
urlpatterns += sensor_urls
urlpatterns += camera_urls
urlpatterns += patient_urls
