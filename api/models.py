from django.db import models
from django import forms

# Create your models here.

class Incubadora(models.Model):
    numero = models.PositiveIntegerField()
    nombre = models.CharField(max_length=200)
    direccion_ip = models.CharField(max_length=200)
    activo = models.BooleanField(default=False)
    
class Camara(models.Model):
    incubadora = models.ForeignKey(Incubadora, related_name='camaras', on_delete=models.CASCADE, null=True)
    numero = models.PositiveIntegerField()
    tipo_camara = models.CharField(max_length=200)
    puerto = models.CharField(max_length=100, null=True, default="")
    activo = models.BooleanField(default=False)
    
class Topic(models.Model):
    nombre = models.CharField(max_length=200)

class Sensor(models.Model):
    incubadora = models.ForeignKey(Incubadora, related_name='sensores', on_delete=models.CASCADE, null=True)
    tipo_sensor = models.ForeignKey(Topic, related_name='sensores', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=200)
    numero = models.PositiveIntegerField()
    activo = models.BooleanField(default=False)
    
class Alarma(models.Model):
    sensor = models.ForeignKey(Sensor, related_name='alarmas', on_delete=models.CASCADE, null=False)
    limite_superior = models.IntegerField()
    limite_inferior = models.IntegerField()
    
class Paciente(models.Model):
    incubadora = models.ForeignKey(Incubadora, related_name='pacientes', on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    apellido1 = models.CharField(max_length=200, default='', blank=True)
    apellido2 = models.CharField(max_length=200, default='', blank=True)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)