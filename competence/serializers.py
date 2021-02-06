from rest_framework import serializers
from .models import Competence, Niveaux

class NiveauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveaux
        fields = ['groupeAction', 'critereEvaluation']

class CompetenceSerializer(serializers.ModelSerializer):
    niveaux = NiveauxSerializer(many=True)
    # groupeCompetence = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='libelle'
    #  )

    class Meta:
        model = Competence
        fields = ['libelle', 'niveaux']

    def create(self, validated_data):
        niveaux_data = validated_data.pop('niveaux')
        competence = Competence.objects.create(**validated_data)
        for niveau_data in niveaux_data:
            Niveaux.objects.create(competence=competence, **niveau_data)
        return competence