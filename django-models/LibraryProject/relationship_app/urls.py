from django.urls import path
from .models import Book, Library
from . import views
from .views import LibraryDetailView, SignUpView
from django.contrib.auth import views

urlpatterns = [
    path("", views.list_books, name='book'),
    path("", LibraryDetailView.as_view(), name="library_detail"),
    path("", SignUpView.as_view(), name='registration'),
    path("login/", views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path('register/',views.register, name="register"),
]
