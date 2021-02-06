from django.urls import path, include
from .views import profilSortie_list, profilSortie_detail

urlpatterns = [
    path('', profilSortie_list.as_view(), name="profils_options"),
    path('<int:pk>/', profilSortie_detail.as_view(), name="profil_detail")
]