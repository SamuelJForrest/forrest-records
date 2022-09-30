from django.contrib import admin
from .models import BlogPage, Blog

# Register your models here.

class BlogPageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'subtitle',
    )

    def has_add_permission(self, request):
        return False


class BlogsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_published',
        'author'
    )
    ordering = ['-id']

admin.site.register(BlogPage, BlogPageAdmin)
admin.site.register(Blog, BlogsAdmin)

