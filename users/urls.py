from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import student_list, MyObtainTokenPairView, Admin_list, Teacher_list, UpdateUser, user_detail, user_list
from groupeCompetence.views import groupeCompetence_list
router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('users/', user_list.as_view(),name="users_options"),
    path('student/', student_list.as_view(),name="students_options"),
    path('teacher/', Teacher_list.as_view(),name="teacher_options"),
    path('admins/', Admin_list.as_view(),name="admin_options"),
    path('users/<int:pk>/update', UpdateUser.as_view(),name="update_options"),
    path('users/<int:pk>/detail', user_detail.as_view(),name="detail_options"),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),

]