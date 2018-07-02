from django.contrib import admin

from example.models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
