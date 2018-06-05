from django.contrib import admin

from example.models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('content_json', 'content_md')

    def has_add_permission(self, request):
        return False
