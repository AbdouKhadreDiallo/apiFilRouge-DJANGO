from django.db import models
from groupeCompetence.models import GroupeCompetence
# Create your models here.
class Competence(models.Model):
    libelle = models.CharField(max_length=250)
    groupeCompetence = models.ManyToManyField(GroupeCompetence, blank=True, related_name="competences")
    
    
    def __str__(self):
        return self.libelle


class Niveaux(models.Model):
    groupeAction = models.CharField(max_length=200)
    critereEvaluation = models.CharField(max_length=200)
    competence = models.ForeignKey(Competence, blank=True, related_name="niveaux", on_delete=models.CASCADE)