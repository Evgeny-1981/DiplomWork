from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрация пользователей в админке."""

    list_display = ("id", "email", "role", "is_active", "password", "image", "phone")
    list_filter = (
        "email",
        "role",
    )
    search_fields = ("email",)
