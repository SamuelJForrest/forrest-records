from django.contrib import admin
from .models import Product, ProductType, ProductGroup, Album, Song, Genre, Merch

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductGroup)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Merch)
