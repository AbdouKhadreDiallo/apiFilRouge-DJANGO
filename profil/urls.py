from django.urls import path, include
from .views import profil_list, profil_detail

urlpatterns = [
    path('', profil_list.as_view(), name="profils_options"),
    path('<int:pk>/', profil_detail.as_view(), name="profil_detail")
]
