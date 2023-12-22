from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login, name='login'),
    path('get-profile/', views.get_profile, name='get-profile'),
    path('get-profile-id/<str:pk>/', views.get_profile_id, name='get-profile-id'),
]
