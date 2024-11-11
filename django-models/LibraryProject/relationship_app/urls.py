from django.urls import path
from .models import Book, Library
from .views import list_books
from .views import LibraryDetailView, SignUpView

urlpatterns = [
    path("", list_books, name='book'),
    path("", LibraryDetailView.as_view(), name="library_detail"),
    path("", SignUpView.as_view(), name='registration')
]
