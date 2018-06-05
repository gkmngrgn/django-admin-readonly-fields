import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from example.models import Test


class Command(BaseCommand):
    USERNAME = 'admin'
    PASSWORD = 'secret'
    EMAIL = 'admin@foo.bar'

    def handle(self, *args, **options):
        if not get_user_model().objects.filter(username=self.USERNAME).exists():
            self.stdout.write(self.style.SUCCESS("Admin user is ready."))
            get_user_model().objects.create_superuser(username=self.USERNAME, password=self.PASSWORD, email=self.EMAIL)

        Test.objects.all().delete()
        with open(os.path.join(settings.BASE_DIR, 'example', 'data', 'test.json')) as content_json_file:
            content_json = content_json_file.read()
        with open(os.path.join(settings.BASE_DIR, 'example', 'data', 'test.md')) as content_md_file:
            content_md = content_md_file.read()

        Test.objects.create(
            content_json=content_json,
            content_md=content_md)

        self.stdout.write(self.style.SUCCESS("Test objects are created successfully."))
