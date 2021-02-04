from django.shortcuts import render
from .models import Profil
from .serializers import ProfilSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
# Create your views here.


class profil_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        profil = Profil.objects.all()
        serializer = ProfilSerializer(profil, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfilSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class profil_detail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            return Profil.objects.get(pk=pk)
        except Profil.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profil = self.get_object(pk)
        serializer = ProfilSerializer(profil)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        profil = self.get_object(pk)
        profil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        profil = self.get_object(pk)
        serializer = ProfilSerializer(profil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)