from django.contrib import admin
from .models import BlogPage, Blogs

# Register your models here.

class BlogPageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

    def has_add_permission(self, request):
        return False


class BlogsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    ordering = ['-id']

admin.site.register(BlogPage, BlogPageAdmin)
admin.site.register(Blogs, BlogsAdmin)

