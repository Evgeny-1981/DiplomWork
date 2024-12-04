# Generated by Django 5.1.3 on 2024-12-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0010_alter_ad_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ad",
            name="price",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Стоимость товара/услуги"
            ),
        ),
    ]