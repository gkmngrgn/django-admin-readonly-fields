import json

from django.forms import fields
from django.template.loader import render_to_string
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


class ReadOnlyInput(fields.TextInput):
    class Media:
        css = {
            'all': ('admin_readonly_fields/admin.css',)
        }
        js = ('admin_readonly_fields/admin.js',)


class ReadOnlyJsonInput(ReadOnlyInput):
    def render(self, name, value, **kwargs):
        formatter = HtmlFormatter(style='colorful', noclasses=True, linenos='table')
        result = json.dumps(json.loads(value), sort_keys=True, indent=4, ensure_ascii=False)
        result = highlight(result, JsonLexer(), formatter)
        return render_to_string('admin_readonly_fields/json.html', {'value': result})


class ReadOnlyMarkdownInput(ReadOnlyInput):
    def render(self, name, value, **kwargs):
        result = mark_safe('<br/>{}'.format(markdown(value)))
        return render_to_string('admin_readonly_fields/md.html', {'value': result})
