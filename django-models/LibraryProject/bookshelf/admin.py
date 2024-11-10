from django.contrib import admin
from .models import Book

# Registration of Book model to admin interface.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=("title","author","publication_year")
    list_filter=("publication_year",)
    search_fields=("title",)