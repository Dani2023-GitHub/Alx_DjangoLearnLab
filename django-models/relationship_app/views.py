from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView

# Create your views here.
def book_lists(request):
    books=Book.objects.all()

    return render(request, template_name='relationship_app/list_books.html')


class LibraryDetailView(DetailView):
    model = Library
    template_name="relationship_app/library_detail.html"
    context_object_name = 'library'
