from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_classes = BookSerializer
