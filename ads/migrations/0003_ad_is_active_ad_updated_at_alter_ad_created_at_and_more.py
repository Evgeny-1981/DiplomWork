# Generated by Django 5.1.3 on 2024-12-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_delete_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="ad",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ad",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="ad",
            name="created_at",
            field=models.DateTimeField(
                auto_now=True,
                null=True,
                verbose_name="Дата и время создания объявления",
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Стоимость"
            ),
        ),
    ]
