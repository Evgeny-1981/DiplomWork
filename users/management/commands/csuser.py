from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@sky.pro",
            first_name="admin",
            last_name="skypro",
            is_staff=True,
            is_superuser=True,
            role='admin',
        )
        user.set_password("1238")
        user.save()
