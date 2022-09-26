from django.contrib import admin
from .models import Homepage


class HomepageAdmin(admin.ModelAdmin):
    """
    Admin settings for homepage model.
    """
    list_display = (
        'title',
        'lead_paragraph',
    )

    def has_add_permission(self, request):
        return False


admin.site.register(Homepage, HomepageAdmin)
