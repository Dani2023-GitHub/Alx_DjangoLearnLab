from django.contrib import admin
from .models import Book

# Registration of Book model to admin interface.
admin.site.register(Book)
