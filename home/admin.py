from django.contrib import admin
from .models import Homepage

# Register your models here.

class HomepageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'lead_paragraph',
    )

    def has_add_permission(self, request):
        return False


admin.site.register(Homepage, HomepageAdmin)
