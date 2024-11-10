
from .models import *

#book query by specific author

def bookQuery(author_name):
    author = Author.objects.get(name=author_name)
    for book in Book.objects.filter(author=author):
        print(f"{book.title}")

#quary of all book in a library
def books_in_library(library_name):
    lib = Library.objects.get(name=library_name)

    for book in lib.books.all():
        print(f"{book.title}")
            
#get list of librarian
def librarian_list(library_name):
    library = Library.objects.get(name=library_name)
    for librarian in Librarian.objects.filter(library=library):
        print(f"{librarian.name}")
