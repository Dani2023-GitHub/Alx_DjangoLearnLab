
from .models import *

#book query by specific author

def bookQuery(author):
    books = Book.objects.select_related('author').all()
    for book in books:
        if book.author == author:
            print(f"{book.title}")

#quary of all book in a library
def books_in_library(library_name):
    lib = Library.objects.get(name = library_name)

    for book in lib:
        print(f"{book.title}")
            
#get list of librarian
def librarian_list(libary):
    librarians = Librarian.objects.select_related("library")
    for librarian in librarians:
        if librarian.library == libary:
            print(f"{librarian.name}")
