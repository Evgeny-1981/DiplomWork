# Generated by Django 5.1.3 on 2024-12-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0004_alter_ad_is_active_alter_ad_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                null=True,
                verbose_name="Дата и время создания объявления",
            ),
        ),
    ]
