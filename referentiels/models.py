from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
fs = FileSystemStorage(location='/media/doc')

class Referentiel(models.Model):
    libelle = models.CharField(max_length=200)
    presentation = models.CharField(max_length=200)
    critereAdmission = models.CharField(max_length=200)
    critereEvaluation = models.CharField(max_length=200)
    programme = models.FileField(upload_to='doc/',null=True, default=None, blank=True)

    def __str__(self):
        return self.libelle
    
