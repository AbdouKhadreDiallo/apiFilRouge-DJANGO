from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from competence.models import Competence
from .models import GroupeCompetence
from .serializers import GroupeCompetenceSrializer
from rest_framework.views import APIView
# Create your views here.


class groupeCompetence_list(viewsets.ModelViewSet):
    serializer_class = GroupeCompetenceSrializer

    def get_queryset(self):
        groupeCompetence = GroupeCompetence.objects.all()
        return groupeCompetence

    def create(self, request, *args, **kwargs):
        data = request.data

        groupe_Competence = GroupeCompetence.objects.create(
            libelle=data["libelle"], descriptif=data['descriptif'])

        groupe_Competence.save()
        
        for module in data["competences"]:
            competObj = Competence.objects.get(libelle=module["libelle"])
            groupe_Competence.competences.add(competObj)

        serializer = GroupeCompetenceSrializer(groupe_Competence)

        return Response(serializer.data)