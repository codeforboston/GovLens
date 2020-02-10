"""Idempotent management command to create the scraper user with a DRF token
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

SCRAPER_USERNAME = "scraper"


class Command(BaseCommand):
    help = "Get or create a scraper user with a Django REST Framework token"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(username=SCRAPER_USERNAME)
        user.save()

        if created:
            self.stdout.write(f"Created new user with username {SCRAPER_USERNAME}")
        else:
            self.stdout.write(f"User {SCRAPER_USERNAME} already exists.")

        token, created = Token.objects.get_or_create(user=user)
        self.stdout.write(f"The token for the user {SCRAPER_USERNAME} is {token}")
