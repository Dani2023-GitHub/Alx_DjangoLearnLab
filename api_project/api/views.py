from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookList(generics.ListAPIView):

    #only authenticated user can view the list
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_classes = BookSerializer

class BookViewSet(viewsets.ModelViewSet):

    #Admin user can perform CRUD operation
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]    
    queryset = Book.objects.all()
    serializer_classes = BookSerializer
