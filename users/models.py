
from django.db import models
from django.contrib.auth.models import AbstractUser
from profil.models import Profil


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='images/',null=True, default=None, blank=True)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE,blank=True,null=True, related_name="user")

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username