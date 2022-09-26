from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin settings for user profiles.
    """

    list_display = (
        'id',
    )


admin.site.register(UserProfile)
