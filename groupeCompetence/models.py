from django.db import models

# Create your models here.
class GroupeCompetence(models.Model):
    libelle = models.CharField(max_length=250)
    descriptif = models.CharField(max_length=250)

    def __str__(self):
        return self.libelle
    
