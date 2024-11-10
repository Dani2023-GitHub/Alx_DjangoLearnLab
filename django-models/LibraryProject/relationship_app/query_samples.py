
from .models import *

#book query by specific author

def bookQuery(author):
    books = Book.objects.select_related('author').all()
    for book in books:
        if book.author == author:
            print(f"{book.title}")

#quary of all book in a library
def books_in_library(library):
    librarys = Library.objects.prefetch_related("books").all()
    if library in librarys:
        for book in library.books.all():
            print(f"{book.title}")
            
#get list of librarian
def librarian_list(libary):
    librarians = Librarian.objects.select_related("library")
    for librarian in librarians:
        if librarian.library == libary:
            print(f"{librarian.name}")
