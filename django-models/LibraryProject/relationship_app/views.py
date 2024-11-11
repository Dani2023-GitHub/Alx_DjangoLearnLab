from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_books(request):
    books=Book.objects.all()

    return render(request, template_name='relationship_app/list_books.html')


class LibraryDetailView(DetailView):
    model = Library
    template_name="relationship_app/library_detail.html"
    context_object_name = 'library'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"
