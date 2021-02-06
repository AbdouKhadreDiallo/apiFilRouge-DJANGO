from django.urls import path, include
from .views import groupeCompetence_list
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", groupeCompetence_list, basename="groupeCompetence")

urlpatterns = [
    path('', include(router.urls))
]
