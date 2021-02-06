from rest_framework import serializers
from .models import ProfilSortie



class ProfilSortieSerializer(serializers.ModelSerializer):
    students = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = ProfilSortie
        fields =('id', 'libelle', 'students')