from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    USERNAME = 'admin'
    PASSWORD = 'secret'
    EMAIL = 'admin@foo.bar'

    def handle(self, *args, **options):
        if get_user_model().objects.filter(username=self.USERNAME).exists():
            return

        get_user_model().objects.create_superuser(username=self.USERNAME, password=self.PASSWORD, email=self.EMAIL)
