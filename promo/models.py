from django.db import models
from referentiels.models import Referentiel
from users.models import Admin, Student, Teacher

# Create your models here.
class Promo(models.Model):
    langue = models.CharField(max_length=200)
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    lieu = models.CharField(max_length=200)
    referenceAgate = models.CharField(max_length=200, null =True)
    dateDebut = models.DateField(auto_now=False)
    dateFinProvisoire = models.DateField(auto_now=False)
    dateFinReelle = models.DateField(auto_now=False, null=True)
    fabrique = models.CharField(max_length=200, default="SONATEL ACADEMY")
    etat = models.CharField(max_length=200, null =True)
    referentiels = models.ManyToManyField(Referentiel, related_name="promo")
    author = models.ForeignKey(Admin, on_delete=models.CASCADE, blank=True, null =True)
    formateurs = models.ManyToManyField(Teacher, related_name="promo", blank=True, null=True)

class Groupe(models.Model):
    nom = models.CharField(max_length=200)
    dateCreation = models.DateField(auto_now=True)
    statut = models.CharField(max_length=200, default="Dispo", null=True)
    type = models.CharField(max_length=200)
    promo = models.ForeignKey(Promo, on_delete=models.CASCADE, blank=True, null = True)
    apprenant = models.ManyToManyField(Student, related_name="groupe")



