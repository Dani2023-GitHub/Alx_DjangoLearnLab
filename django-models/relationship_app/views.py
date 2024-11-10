from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.
def book_lists(request):
    books=Book.objects.all()

    return render(request, template_name='templates/book_lists.html')


class LibraryDetailView(DetailView):
    model = Library
    template_name="library_detail.html"
    context_object_name = 'library'
