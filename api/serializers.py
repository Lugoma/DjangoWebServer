from rest_framework import serializers
from .models import *

class IncubadoraSerializer(serializers.ModelSerializer):
    camaras = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    pacientes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Incubadora
        fields = ('__all__')

class CamaraSerializer(serializers.ModelSerializer):
    incubadora = serializers.PrimaryKeyRelatedField(required=False, queryset=Incubadora.objects.all(), many=False)
    videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Camara
        fields = ('__all__')

class TopicSerializer(serializers.ModelSerializer):
    sensores = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Topic
        fields = ('__all__')

class SensorSerializer(serializers.ModelSerializer):
    incubadora = serializers.PrimaryKeyRelatedField(required=False, queryset=Incubadora.objects.all(), many=False)
    tipo_sensor = serializers.PrimaryKeyRelatedField(required=False, queryset=Topic.objects.all(), many=False)
    alarmas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Sensor
        fields = ('__all__')
        
class AlarmaSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(required=True, queryset=Sensor.objects.all(), many=False)
    
    class Meta:
        model = Alarma
        fields = ('__all__')

class PacienteSerializer(serializers.ModelSerializer):
    incubadora = serializers.PrimaryKeyRelatedField(required=False, queryset=Incubadora.objects.all(), many=False, allow_null=True)
    fecha_nacimiento = serializers.DateTimeField(format("%Y-%m-%d"))
    
    class Meta:
        model = Paciente
        fields = ('__all__')
