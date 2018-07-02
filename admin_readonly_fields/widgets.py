import json

from django.forms import fields
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.data import JsonLexer

try:
    from markdown import markdown
except ImportError:
    def markdown(*args, **kwargs):
        raise Exception("Check your installation for Markdown support.")

__all__ = [
    'ReadOnlyJsonInput',
    'ReadOnlyMarkdownInput'
]


class ReadOnlyJsonInput(fields.TextInput):
    def render(self, name, value, **kwargs):
        formatter = HtmlFormatter(style='colorful', noclasses=True)
        response = json.dumps(value, sort_keys=True, indent=4, ensure_ascii=False)
        response = highlight(response, JsonLexer(), formatter)
        return mark_safe('<br/>{}'.format(response))


class ReadOnlyMarkdownInput(fields.TextInput):
    def render(self, name, value, **kwargs):
        return mark_safe('<br/>{}'.format(markdown(value)))
