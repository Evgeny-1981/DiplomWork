# Generated by Django 5.1.3 on 2024-12-01 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0007_alter_ad_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ad",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="ad",
            name="updated_at",
        ),
    ]
