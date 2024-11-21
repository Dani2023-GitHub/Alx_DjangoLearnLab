from django.shortcuts import render, redirect

from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test


# Create your views here.
def book_list(request):
    books=Book.objects.all()

    

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request):
   pass

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    pass

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    pass

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request, pk):
    pass

