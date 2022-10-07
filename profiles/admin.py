from django.contrib import admin
from .models import UserProfile, Wishlist


class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin settings for user profiles.
    """

    list_display = (
        'user',
        'id',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Wishlist)
