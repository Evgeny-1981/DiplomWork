from django.contrib import admin

from ads.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """Регистрация объявлений в админке."""

    list_display = (
        "id",
        "title",
        "price",
        "description",
        "author",
        "created_at",
    )
    list_filter = (
        "title",
        "price",
        "author",
        "created_at",
    )
    # search_fields = ("title", "description",)
