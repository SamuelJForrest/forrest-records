from django.contrib import admin
from .models import Product, ProductType, ProductGroup, Album, Song, Genre, Merch

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'artist',
        'on_sale'
    )

    def has_add_permission(self, request):
        return False

class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'artist',
        'on_sale'
    )

class MerchAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'artist',
        'on_sale'
    )

class SongAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'duration',
        'album',
        'artist',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(ProductGroup)
admin.site.register(Genre)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Merch, MerchAdmin)
