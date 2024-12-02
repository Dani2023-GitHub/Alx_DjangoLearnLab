from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class ListBookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailBookView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateBookview(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteBookCiew(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
