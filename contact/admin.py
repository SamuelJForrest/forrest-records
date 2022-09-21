from django.contrib import admin
from .models import ContactPage

# Register your models here.

class ContactPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

admin.site.register(ContactPage, ContactPageAdmin)
