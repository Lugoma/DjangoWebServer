from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import IncubadoraSerializer, SensorSerializer, CamaraSerializer, PacienteSerializer
from ..models import Incubadora, Sensor, Camara, Paciente
from django.shortcuts import get_object_or_404

class IncubadoraViews(APIView):
    def post(self, request):
        serializer = IncubadoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Incubadora.objects.get(id=id)
            serializer = IncubadoraSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Incubadora.objects.all()
        serializer = IncubadoraSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        item = Incubadora.objects.get(id=id)
        serializer = IncubadoraSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self, request, id=None):
        item = get_object_or_404(Incubadora, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
    
class IncubadoraSensorViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Sensor.objects.filter(incubadora=id)
            serializer = SensorSerializer(item, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class IncubadoraSensorActivoViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Sensor.objects.filter(incubadora=id, activo=True)
            serializer = SensorSerializer(item, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class IncubadoraCamaraViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Camara.objects.filter(incubadora=id)
            serializer = CamaraSerializer(item, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
class IncubadoraActivaViews(APIView):
    def get(self, request, id=None):
        item = Incubadora.objects.filter(activo=True)
        serializer = IncubadoraSerializer(item, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class IncubadoraPacienteViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Paciente.objects.filter(incubadora=id).first()
            serializer = PacienteSerializer(item, many=False)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_400_BAD_REQUEST)

