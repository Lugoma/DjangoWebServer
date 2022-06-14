from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import PacienteSerializer, IncubadoraSerializer
from ..models import Paciente, Incubadora
from django.shortcuts import get_object_or_404

class PacienteViews(APIView):
    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id=None):
        if id:
            item = Paciente.objects.get(id=id)
            serializer = PacienteSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Paciente.objects.all()
        serializer = PacienteSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Paciente.objects.get(id=id)
        serializer = PacienteSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self, request, id=None):
        item = get_object_or_404(Paciente, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
class PacienteIncubadoraViews(APIView):
    def get(self, request, id=None):
        if id:
            paciente = Paciente.objects.get(id=id)
            if(paciente.incubadora):
                item = Incubadora.objects.get(id=paciente.incubadora.id)
                serializer = IncubadoraSerializer(item)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": "Item not found"}, status=status.HTTP_400_BAD_REQUEST)
