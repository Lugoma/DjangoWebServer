from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import SensorSerializer, AlarmaSerializer, TopicSerializer
from ..models import Sensor, Alarma, Topic
from django.shortcuts import get_object_or_404

class SensorViews(APIView):
    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id=None):
        if id:
            item = Sensor.objects.get(id=id)
            serializer = SensorSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Sensor.objects.all()
        serializer = SensorSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Sensor.objects.get(id=id)
        serializer = SensorSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self, request, id=None):
        item = get_object_or_404(Sensor, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
    
class AlarmaViews(APIView):
    def post(self, request):
        serializer = AlarmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id=None):
        if id:
            item = Alarma.objects.get(id=id)
            serializer = AlarmaSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Alarma.objects.all()
        serializer = AlarmaSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Alarma.objects.get(id=id)
        serializer = AlarmaSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self, request, id=None):
        item = get_object_or_404(Alarma, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
class TopicViews(APIView):
    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id=None):
        if id:
            item = Topic.objects.get(id=id)
            serializer = TopicSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Topic.objects.all()
        serializer = TopicSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Topic.objects.get(id=id)
        serializer = TopicSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
class SensorAlarmaViews(APIView):
    def get(self, request, id=None):
        if id:
            item = Alarma.objects.filter(sensor=id).first()
            serializer = AlarmaSerializer(item, many=False)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_400_BAD_REQUEST)
    