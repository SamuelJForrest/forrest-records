from django.contrib import admin
from .models import Product, ProductType, Album, Song, Genre, Merch


class AlbumInline(admin.TabularInline):
    model = Album


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

    ordering = ('id',)


class MerchInline(admin.TabularInline):
    model = Merch


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

    ordering = ('id', )


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

    # inlines = [
    #     AlbumInline,
    #     MerchInline
    # ]

    def has_add_permission(self, request):
        return False


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(Genre)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Merch, MerchAdmin)
