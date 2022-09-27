from django.contrib import admin
from .models import Product, ProductType, ProductGroup, Album, Song, Genre, Merch


class ProductAdmin(admin.ModelAdmin):
    """
    Admin settings for products.
    """
    list_display = (
        'name',
        'id',
        'sku',
        'price',
        'artist',
        'on_sale'
    )

    def has_add_permission(self, request):
        return False


class AlbumAdmin(admin.ModelAdmin):
    """
    Admin settings for albums.
    """
    list_display = (
        'name',
        'id',
        'sku',
        'price',
        'artist',
        'on_sale'
    )


class MerchAdmin(admin.ModelAdmin):
    """
    Admin settings for merch.
    """
    list_display = (
        'name',
        'id',
        'sku',
        'price',
        'artist',
        'on_sale'
    )


class SongAdmin(admin.ModelAdmin):
    """
    Admin settings for songs.
    """
    list_display = (
        'title',
        'track_number',
        'duration',
        'album',
        'artist',
    )

    ordering = ('album', 'track_number')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(ProductGroup)
admin.site.register(Genre)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Merch, MerchAdmin)
