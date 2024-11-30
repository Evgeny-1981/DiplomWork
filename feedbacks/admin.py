from django.contrib import admin

from feedbacks.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Регистрация отзывов в админке."""

    list_display = (
        "id",
        "text",
        "author",
        "ad",
        "created_at",
    )
    list_filter = (
        "text",
        "author",
        "ad",
        "created_at",
    )
    search_fields = ("author", "text", "created_at",)
