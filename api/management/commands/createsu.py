import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin_username = os.getenv("DJANGO_ADMIN_USERNAME")
        admin_email = os.getenv("DJANGO_ADMIN_EMAIL")
        admin_password = os.getenv("DJANGO_ADMIN_PASSWORD")
        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(admin_username, admin_email, admin_password)
            self.stdout.write(self.style.SUCCESS("Successfully created superuser"))
