from django.contrib import admin
from bookshelf.models import Book

# Registration of Book model to admin interface.
admin.site.register(Book)
