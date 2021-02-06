from django.urls import path, include
from .views import Competence_list

urlpatterns = [
    path('', Competence_list.as_view(), name="competence_options")
]
