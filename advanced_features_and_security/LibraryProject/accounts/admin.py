from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Show extra fields in admin list
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "date_of_birth")
    list_filter = ("is_staff", "is_superuser", "is_active")

    # Add extra fields to the user detail page (edit form)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Add extra fields to the create-user page in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    search_fields = ("username", "email")
    ordering = ("username",)