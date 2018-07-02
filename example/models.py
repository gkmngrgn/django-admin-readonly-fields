from django.db import models

from admin_readonly_fields import ReadOnlyJsonField, ReadOnlyMarkdownField


class Test(models.Model):
    content_json = ReadOnlyJsonField()
    content_md = ReadOnlyMarkdownField()

    def __str__(self):
        return 'Test {}'.format(self.id)
