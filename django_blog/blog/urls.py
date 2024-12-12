from django.urls import path
from .views import (
    RegistrationView, ProfileView, CustomLoginView, CustomLogoutView
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),    
]
