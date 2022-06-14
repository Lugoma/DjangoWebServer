from django.urls import path
from .views import *
from .incubator.urls import urlpatterns as incubator_urls
from .sensor.urls import urlpatterns as sensor_urls
from .camera.urls import urlpatterns as camera_urls
from .patient.urls import urlpatterns as patient_urls
# se pueden crear los paths en otro modulo y hacer include() de este modulo

# para empezar a hacer operaciones complejas como acceder a la lista de pacientes de un medico hace falta emplear
# una nueva uri y crearla aqui del tipo persona/{id}/paciente
# si a esta uri se le aniade una id al paciente entonces trae el paciente concreto, pero es absurdo, teniendo la id
# hay que dividir las urls en diferentes ficheros (y rutas) por cada tabla, para no tenerlo todo junto
urlpatterns = [
    # aqui podria ir la de login por ejemplo
    # o cosas de configuracion
]

urlpatterns += incubator_urls
urlpatterns += sensor_urls
urlpatterns += camera_urls
urlpatterns += patient_urls
