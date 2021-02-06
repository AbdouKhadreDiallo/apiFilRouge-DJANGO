from django.urls import path, include
from .views import ReferentielViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", ReferentielViewSet, basename="referentiel")

urlpatterns = [
    path('', include(router.urls))
]