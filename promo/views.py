from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from users.models import Student, User
from rest_framework import viewsets
from .serializers import PromoSerializer
from referentiels.models import Referentiel
from .models import Promo, Groupe
from ApiFilRougeDjango.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.
class Promo_list(viewsets.ModelViewSet):
    serializer_class = PromoSerializer

    def get_queryset(self):
        promo = Promo.objects.all()
        return promo
    def create(self, request, *args, **kwargs):
        data = request.data

        promo = Promo.objects.create(
            langue=data['langue'],
            description=data['description'],
            titre=data['titre'],
            lieu=data['lieu'],
            referenceAgate=data['referenceAgate'],
            dateDebut=data['dateDebut'],
            dateFinProvisoire=data['dateFinProvisoire'],
            etat=data['etat']
        )
        groupe = Groupe.objects.create(nom="Groupe1", type="Principal", promo=promo)
        for std in data['student']:
            user = User.objects.create(
                username= std['email'].split('@')[0],
                email = std['email']
            )
            subject = 'Welcome to Fil Rouge Project'
            message = "Here are your credentials: \n username: {} \n password: {}".format(std['email'].split('@')[0], "password")
            recipient = std['email']
            user.set_password("password")
            user.is_student=True
            user.profil_id=3
            user.save()
            student = Student.objects.create(user=user)
            send_mail(subject,message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            groupe.apprenant.add(student)
        promo.save()
        for ref in data['referentiels']:
            refObj = Referentiel.objects.get(libelle=ref['libelle'])
            promo.referentiels.add(refObj)
        

        
        serializer = PromoSerializer(promo)
        return  Response(serializer.data)
    
    
