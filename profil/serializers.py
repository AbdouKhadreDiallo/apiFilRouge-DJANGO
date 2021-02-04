from rest_framework import serializers
from .models import Profil



class ProfilSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
     )

    class Meta:
        model = Profil
        fields =('id', 'libelle', 'user')