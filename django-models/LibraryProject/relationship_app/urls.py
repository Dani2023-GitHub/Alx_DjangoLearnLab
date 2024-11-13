from django.urls import path
from .models import Book, Library
from . import views as view1
from .views import LibraryDetailView, SignUpView, admin_view, librarian_view, member_view
from django.contrib.auth import views

urlpatterns = [
    path("", view1.list_books, name='book'),
    path("", LibraryDetailView.as_view(), name="library_detail"),
    path("", SignUpView.as_view(), name='registration'),
    path("login/", views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path('register/',view1.register, name="register"),
    path('admin/', admin_view, name="admin"),
    path("librarian/", librarian_view, name="librarian"),
    path("member/", member_view, name="member")
]
