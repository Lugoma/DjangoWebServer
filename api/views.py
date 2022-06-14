from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
# hay que dividir las vistas por tablas o por relaciones para no tenerlo todo junto
# hay que crear una vista por cada url que se quiera usar, o combinaciones de ambas, para no hacerlo un lio

# en cada clave foranea que haya, comprobar si es null o no(depende si puede serlo) y guardar la referencia,
# objeto en la tabla que corresponde:
# from blog.models import Blog, Entry
# entry = Entry.objects.get(pk=1)
# cheese_blog = Blog.objects.get(name="Cheddar Talk")
# entry.blog = cheese_blog
# entry.save()
# https://docs.djangoproject.com/en/4.0/topics/db/queries/
    
