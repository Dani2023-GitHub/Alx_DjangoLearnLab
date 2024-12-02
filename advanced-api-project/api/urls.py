from django.urls import path
from .views import (
    BookCreateView,
    BookListView,
    BookDetailView,
    BookDeleteView,
    BookUpdateView
)

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookCreateView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/<int:pk>/', BookUpdateView.as_view()),
    path('books/<int:pk>/', BookDeleteView.as_view()),
]
