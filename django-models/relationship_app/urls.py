from django.urls import path
from .models import Book, Library
from . import views

urlpatterns = [
    path("", views.book_lists, name='book'),
    path("", views.LibraryDetailView.as_view(), name="library_detail"),
]
