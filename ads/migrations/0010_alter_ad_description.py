# Generated by Django 5.1.3 on 2024-12-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0009_alter_ad_description_alter_ad_price_alter_ad_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="description",
            field=models.TextField(
                blank=True,
                default="Автор пока не создал описания",
                null=True,
                verbose_name="Описание",
            ),
        ),
    ]