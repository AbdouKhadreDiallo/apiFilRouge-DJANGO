from django.shortcuts import render
from .models import Competence
from .serializers import CompetenceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class Competence_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        users = Competence.objects.all()
        serializer = CompetenceSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompetenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)