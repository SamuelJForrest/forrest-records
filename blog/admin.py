from django.contrib import admin
from .models import BlogPage, Blog


class BlogPageAdmin(admin.ModelAdmin):
    """
    Blog page admin setup
    """
    list_display = (
        'title',
        'subtitle',
    )

    def has_add_permission(self, request):
        return False


class BlogsAdmin(admin.ModelAdmin):
    """
    Individual blogs admin setup
    """
    list_display = (
        'title',
        'date_published',
        'author'
    )
    ordering = ['-id']


admin.site.register(BlogPage, BlogPageAdmin)
admin.site.register(Blog, BlogsAdmin)
