 
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import status, viewsets, generics
from .models import User, Student, Admin, Teacher
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentRegisterSerializer,MyTokenObtainPairSerializer, TeacherRegisterSerializer, AdminRegisterSerializer,CustomUserSerializer,UpdateUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import Http404


class user_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class student_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        users = User.objects.all().filter(is_student=True)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Teacher_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        users = User.objects.all().filter(is_teacher=True)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Admin_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        users = User.objects.all().filter(is_admin=True)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdminRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user_detail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class UpdateUser(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer