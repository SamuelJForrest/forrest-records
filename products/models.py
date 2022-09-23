from django.db import models

from artists.models import Artist

# Create your models here.

class ProductType(models.Model):

    name = models.CharField(max_length=254, null=False, blank=False)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductGroup(models.Model):
    
    name = models.CharField(max_length=254, null=False, blank=False)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    
    name = models.CharField(max_length=254, null=False, blank=False)
    sku = models.CharField(max_length=254, null=True, blank=False)
    description = models.TextField()
    product_type = models.ForeignKey('ProductType', default=1, null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Artist, default=1, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    rating = models.IntegerField(null=True, blank=True, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    product_group = models.ForeignKey('ProductGroup', default=1, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(max_length=254, null=False, blank=False)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Album(Product):

    record_label = models.CharField(max_length=254, null=True, blank=True)
    release_year = models.CharField(max_length=4, null=True, blank=True)
    genre = models.ForeignKey('Genre', default=1, null=True, blank=True, on_delete=models.SET_NULL)
    digital_download = models.BooleanField(default=True, null=True, blank=True)
    digital_download_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):

    title = models.CharField(max_length=254, null=False, blank=False)
    album = models.ForeignKey('Album', default=1, null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Artist, default=1, null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.CharField(max_length=6, null=True, blank=True)
    track_number = models.CharField(max_length=3, null=False, blank=False)

    def __str__(self):
        return self.title


class Merch(Product):
    class Meta:
        verbose_name_plural = 'Merch'

    has_sizes = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.name
