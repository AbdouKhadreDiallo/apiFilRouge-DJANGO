from django.shortcuts import render
from .serializers import ReferentielSerializers
from .models import Referentiel
from rest_framework import viewsets
# Create your views here.

class ReferentielViewSet(viewsets.ModelViewSet):
    serializer_class = ReferentielSerializers

    def get_queryset(self):
        referentiel = Referentiel.objects.all()
        return referentiel