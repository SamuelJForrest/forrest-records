from django.contrib import admin
from .models import ContactPage, Message


class ContactPageAdmin(admin.ModelAdmin):
    """
    Admin settings for contact page.
    """
    list_display = (
        'title',
        'subtitle',
    )

    def has_add_permission(self, request):
        return False


class MessageAdmin(admin.ModelAdmin):
    """
    Admin settings from messages.
    """
    list_display = (
        'name',
        'id',
        'email',
        'message'
    )


admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(Message, MessageAdmin)
