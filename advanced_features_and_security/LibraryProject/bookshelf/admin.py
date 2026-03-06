from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 1) Show these columns in the admin list view
    list_display = ("title", "author", "publication_year")

    # 2) Add filter sidebar options
    list_filter = ("author", "publication_year")

    # 3) Add a search box (search by title or author)
    search_fields = ("title", "author")