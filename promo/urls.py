from django.urls import path, include
from .views import Promo_list
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", Promo_list, basename="promo")

urlpatterns = [
    path('', include(router.urls))
]