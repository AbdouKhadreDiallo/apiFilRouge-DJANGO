from django.db import models

# Create your models here.
class ProfilSortie(models.Model):
    libelle = models.CharField(max_length = 200, unique=True)
    def __str__(self):
        return self.libelle