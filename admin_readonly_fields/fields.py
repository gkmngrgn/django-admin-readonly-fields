from django.db import models

from admin_readonly_fields.widgets import *

__all__ = [
    'ReadOnlyJsonField',
    'ReadOnlyMarkdownField'
]


class ReadOnlyField(models.TextField):
    widget = None

    def __init__(self, *args, **kwargs):
        super(ReadOnlyField, self).__init__(*args, **kwargs)
        kwargs['editable'] = True  # it should be always true to use `render` function.

    def formfield(self, **kwargs):
        defaults = kwargs
        if self.widget is not None:
            defaults['widget'] = self.widget
        return super(ReadOnlyField, self).formfield(**defaults)


class ReadOnlyJsonField(ReadOnlyField):
    widget = ReadOnlyJsonInput


class ReadOnlyMarkdownField(ReadOnlyField):
    widget = ReadOnlyMarkdownInput
