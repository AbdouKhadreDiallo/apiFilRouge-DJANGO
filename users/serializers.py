
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db import transaction
from .functions import decodeDesignImage
from .models import User, Student, Teacher, Admin
import base64
from django.core.files.base import ContentFile




class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    profil = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='libelle'
    )
    class Meta:
        model = User
        fields = ('email', 'username', 'password','first_name', 'last_name','avatar' )
        lookup_field="profil"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class StudentRegisterSerializer(serializers.ModelSerializer):
    # profil = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='libelle'
    # )
    class Meta:
        model = User
        fields = fields = ('email', 'username', 'password','first_name', 'last_name', 'avatar',)
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_student = True
        instance.profil_id= 3
        if password is not None:
            instance.set_password(password)
        instance.save()
        student = Student.objects.create(user=instance)
        return instance

class TeacherRegisterSerializer(serializers.ModelSerializer):
    profil = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='libelle'
    )
    class Meta:
        model = User
        fields = fields = ('email', 'username', 'password','first_name', 'last_name', 'avatar',)
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.profil_id= 2
        instance.is_teacher = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        student = Teacher.objects.create(user=instance)
        return instance

class AdminRegisterSerializer(serializers.ModelSerializer):
    profil = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='libelle'
    )
    class Meta:
        model = User
        fields = fields = ('email', 'username', 'password','first_name', 'last_name', 'avatar',)
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.profil_id= 1
        instance.is_admin = True
        instance.is_staff = True
        instance.is_superuser = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        student = Admin.objects.create(user=instance)
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        if user.is_student == True:
            token['type'] = 'student'
        elif user.is_teacher == True:
            token['type'] = 'teacher'
       
        else:
            token['type'] = 'aute que admin'
        return token

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'username': {'required': False},
        }

    def update(self, instance, validated_data):
       instance.__dict__.update(validated_data)
       instance.save()
       return instance