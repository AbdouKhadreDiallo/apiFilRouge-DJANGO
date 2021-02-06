from rest_framework import serializers
from .models import Referentiel

class ReferentielSerializers(serializers.ModelSerializer):
    class Meta:
        model = Referentiel
        fields = '__all__'
        