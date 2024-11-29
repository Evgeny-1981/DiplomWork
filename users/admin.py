from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрация пользователей в админке."""

    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_active",
        "image",
        "phone",
    )
    list_filter = (
        "email",
        "last_name",
        "role",
    )
    search_fields = ("email", "last_name",)
