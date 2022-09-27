from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    """
    Admin settings for the artist model.
    """
    list_display = (
        'friendly_name',
        'id'
    )
    ordering = ('friendly_name',)


admin.site.register(Artist, ArtistAdmin)
