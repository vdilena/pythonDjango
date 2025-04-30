from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Especificamos que queremos que sea visible desde el panel
    list_display = ['title', 'author', 'year']
