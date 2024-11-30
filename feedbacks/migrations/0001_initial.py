# Generated by Django 5.1.3 on 2024-11-30 09:44

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ads", "0002_delete_feedback"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(max_length=400, verbose_name="текст отзыва")),
                (
                    "created_at",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Дата и время отзыва",
                    ),
                ),
                (
                    "ad",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ad_feedback",
                        to="ads.ad",
                        verbose_name="Объявление, под которым оставлен отзыв",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_feedback",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь, оставивший отзыв",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
                "db_table": "feedbacks",
                "ordering": ("author", "created_at"),
            },
        ),
    ]
