from django.test import TestCase
from django.urls import reverse, resolve
from .models import Product, ProductType, Album, Merch, Song, Genre
from .views import *
from .forms import AlbumForm, MerchForm

# Models testing

class TestProductModels(TestCase):
    """
    Test Product models
    """

    def test_create_product_model(self):
        """
        Create a test product model
        """
        model = Product(
            name='test',
            price=10,
        )
        self.assertTrue(model.name, model.price)

    def test_create_product_type_model(self):
        """
        Create a test product type model
        """
        model = ProductType(
            name='product_type',
            friendly_name='product type'
        )
        self.assertTrue(model.name, model.friendly_name)

    def test_create_album_model(self):
        """
        Create a test album model
        """
        model = Album(
            name='album',
            price=100
        )
        self.assertTrue(model.name, model.price)

    def test_create_merch_model(self):
        """
        Create a test merch model
        """
        model = Merch(
            name='merch',
            price=200,
            has_sizes=True
        )
        self.assertTrue([model.name, model.price, model.has_sizes])

    def test_genre_model(self):
        """
        Create a test genre model
        """
        model = Genre(
            name='choir',
            friendly_name='choir'
        )
        self.assertTrue([model.name, model.friendly_name])

    def test_song_model(self):
        """
        Create a test song model
        """
        model = Song(
            title='song'
        )
        self.assertTrue(model.title)


# Url test
class TestProductUrls(TestCase):
    """
    Test the product URLs
    """
    def test_all_products_url(self):
        """
        Test all products url
        """
        url = reverse('products')
        self.assertEqual(resolve(url).func, all_products)

    def test_add_album_url(self):
        """
        Test add album url
        """
        url = reverse('add_album')
        self.assertEqual(resolve(url).func, add_album)

    def test_add_merch_url(self):
        """
        Test add merch url
        """
        url = reverse('add_merch')
        self.assertEqual(resolve(url).func, add_merch)

    def test_edit_album_url(self):
        """
        Test add merch url
        """
        url = reverse('edit_album', args=[1])
        self.assertEqual(resolve(url).func, edit_album)

    def test_edit_merch_url(self):
        """
        Test add merch url
        """
        url = reverse('edit_merch', args=[1])
        self.assertEqual(resolve(url).func, edit_merch)

    def test_delete_album_url(self):
        """
        Test add merch url
        """
        url = reverse('delete_album', args=[1])
        self.assertEqual(resolve(url).func, delete_album)

    def test_delete_merch_url(self):
        """
        Test add merch url
        """
        url = reverse('delete_merch', args=[1])
        self.assertEqual(resolve(url).func, delete_merch)

    def test_album_warning_url(self):
        """
        Test add merch url
        """
        url = reverse('album_warning', args=[1])
        self.assertEqual(resolve(url).func, album_warning)

    def test_merch_warning_url(self):
        """
        Test add merch url
        """
        url = reverse('merch_warning', args=[1])
        self.assertEqual(resolve(url).func, merch_warning)

# Form tests

class TestProductForms(TestCase):
    """
    Test product forms
    """
    def test_album_form(self):
        """
        Test album form
        """
        form = AlbumForm({
            'name': 'album2',
            'price': 10,
        })
        self.assertTrue(form)
    
    def test_merch_form(self):
        """
        Test merch form
        """
        form = MerchForm({
            'name': 'album2',
            'price': 10,
            'has_sizes': True
        })
        self.assertTrue(form)
