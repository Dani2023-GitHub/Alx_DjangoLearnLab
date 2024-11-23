from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Registration of Book model to admin interface.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=("title","author","publication_year")
    list_filter=("publication_year",)
    search_fields=("title",)

class CustomUserAdmin(UserAdmin):
    model = CustomUser()
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)