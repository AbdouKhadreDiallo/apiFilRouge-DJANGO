from django.shortcuts import render
from .models import ProfilSortie
from .serializers import ProfilSortieSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from django.http.response import Http404
# Create your views here.


class profilSortie_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        profil = ProfilSortie.objects.all()
        serializer = ProfilSortieSerializer(profil, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfilSortieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class profilSortie_detail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            return ProfilSortie.objects.get(pk=pk)
        except ProfilSortie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        profilSortie = self.get_object(pk)
        serializer = ProfilSortieSerializer(profilSortie)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        profilSortie = self.get_object(pk)
        profilSortie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        profilSortie = self.get_object(pk)
        serializer = ProfilSortieSerializer(profilSortie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)