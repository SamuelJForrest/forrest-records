import math
from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from artists.models import Artist


class ProductType(models.Model):
    """
    Model for product types.
    """

    name = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )

    friendly_name = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        """
        Returns friendly version of the product type name for users.
        """
        return self.friendly_name


class Product(models.Model):
    """
    Model for all products.
    """

    name = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )

    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    description = models.TextField()

    product_type = models.ForeignKey(
        'ProductType',
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    artist = models.ForeignKey(
        Artist,
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False
    )

    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        help_text='If you have your image hosted anywhere else, add the link here to server as a backup.'
    )

    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True
    )

    on_sale = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Model for genres.
    """

    name = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )

    friendly_name = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.friendly_name

    def get_friendly_name(self):
        """
        Returns friendly version of the product type name for users.
        """
        return self.friendly_name


class Album(Product):
    """
    Model for albums - extended from product model.
    """

    record_label = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    release_year = models.CharField(
        max_length=4,
        null=True,
        blank=True
    )

    genre = models.ForeignKey(
        'Genre',
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    digital_download = models.BooleanField(
        default=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def calculate_sale_price(self):
        """
        Calculate the sale price of the product.
        """
        if self.on_sale:
            self.sale_price = round(
                (float(self.price) * settings.SALE_PERCENTAGE), 2)

        return self.sale_price


class Song(models.Model):
    """
    Model for songs.
    """

    title = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )

    album = models.ForeignKey(
        'Album',
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    artist = models.ForeignKey(
        Artist,
        default=1,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    duration = models.CharField(
        max_length=6,
        null=True,
        blank=True
    )

    track_number = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ],
        null=False,
        blank=False
    )

    def __str__(self):
        return self.title


class Merch(Product):
    """
    Model for merch - extended from product model.
    """
    class Meta:
        """
        Admin settings for merch model.
        """
        verbose_name_plural = 'Merch'

    has_sizes = models.BooleanField(
        default=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

    def calculate_sale_price(self):
        """
        Calculate the sale price of the product.
        """

        if self.on_sale:
            self.sale_price = round(
                (float(self.price) * settings.SALE_PERCENTAGE), 2)

        return self.sale_price
