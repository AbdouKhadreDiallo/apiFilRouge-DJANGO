from rest_framework import serializers
from .models import GroupeCompetence
from competence.serializers import CompetenceSerializer

class GroupeCompetenceSrializer(serializers.ModelSerializer):
    class Meta:
        model = GroupeCompetence
        fields = ['libelle', 'descriptif', 'competences']