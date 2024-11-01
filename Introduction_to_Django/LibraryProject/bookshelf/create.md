<!--creation of book instance -->

python manage.py shell
from bookshelf.models import Book
book1 = Book(title="1984", author="George Orwell", publication_year= 1949)
book1.save()
