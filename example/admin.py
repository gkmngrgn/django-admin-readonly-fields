from django.contrib import admin

from example.models import Test


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

    def has_add_permission(self, request):
        return False
