from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


@admin.register(User)
class MyUserAdmin(BaseUserAdmin):
    list_display = ("id", "first_name", "phone", "last_name", "email", "is_staff")
    ordering = ("phone",)

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("first_name", "last_name", "phone", "email", "password1", "password2"),
        }),
    )
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "phone", "email", "password")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )