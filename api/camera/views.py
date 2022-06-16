from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CamaraSerializer
from ..models import Camara
from django.shortcuts import get_object_or_404

class CamaraViews(APIView):
    def post(self, request):
        serializer = CamaraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, id=None):
        if id:
            item = Camara.objects.get(id=id)
            serializer = CamaraSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Camara.objects.all()
        serializer = CamaraSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Camara.objects.get(id=id)
        serializer = CamaraSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self, request, id=None):
        item = get_object_or_404(Camara, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
        