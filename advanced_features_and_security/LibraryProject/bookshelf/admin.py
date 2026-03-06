from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Book
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 1) Show these columns in the admin list view
    list_display = ("title", "author", "publication_year")

    # 2) Add filter sidebar options
    list_filter = ("author", "publication_year")

    # 3) Add a search box (search by title or author)
    search_fields = ("title", "author")


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # show extra fields in admin list
    list_display = ("username", "email", "date_of_birth", "is_staff")

    # add custom fields to the user edit page
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # add custom fields to the user creation page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)