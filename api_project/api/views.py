from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_classes = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_classes = BookSerializer
