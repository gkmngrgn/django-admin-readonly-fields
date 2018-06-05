from django.db import models


class Test(models.Model):
    content_json = models.TextField(editable=False)
    content_md = models.TextField(editable=False)

    def __str__(self):
        return 'Test {}'.format(self.id)
