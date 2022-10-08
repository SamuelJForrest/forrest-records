from django.test import TestCase
from django.urls import reverse, resolve
from .views import add_artist, edit_artist, artist_warning, delete_artist
from .models import Artist
from .forms import ArtistForm


class TestArtistViews(TestCase):
    """
    Tests artist views
    """

    def test_get_artist_page(self):
        """
        Test Artist page
        """
        response = self.client.get('/artists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artists/artists.html')

    def test_get_add_artist_page(self):
        """
        Test add Artist page
        """
        url = reverse('add_artist')
        self.assertEqual(resolve(url).func, add_artist)

    def test_get_edit_artist_page(self):
        """
        Test edit Artist page
        """
        url = reverse('edit_artist', args=[1])
        self.assertEqual(resolve(url).func, edit_artist)

    def test_get_artist_warning_page(self):
        """
        Test Artist warning page
        """
        url = reverse('artist_warning', args=[1])
        self.assertEqual(resolve(url).func, artist_warning)

    def test_get_delete_artist_page(self):
        """
        Test delete Artist page
        """
        url = reverse('delete_artist', args=[1])
        self.assertEqual(resolve(url).func, delete_artist)


class TestArtistModels(TestCase):
    """
    Tests the artist models
    """

    def test_create_artist_models(self):
        """
        Create test artist model
        """
        item = Artist.objects.create(
            name='testing',
            friendly_name='Testing'
        )
        self.assertTrue(item.name, item.friendly_name)

    def test_delete_artist_models(self):
        """
        Create test artist model
        """
        item = Artist.objects.all().delete()


class TestArtistForm(TestCase):
    """
    Tests for artist form
    """

    def test_artist_name_is_required(self):
        """
        Test to see if artist name field is required
        """
        form = ArtistForm({'name': ''})
        self.assertFalse(form.is_valid())

    def test_artist_friendly_name_is_required(self):
        """
        Test to see if artist friendly_name field is required
        """
        form = ArtistForm({'friendly_name': ''})
        self.assertFalse(form.is_valid())

    def test_add_artist_form(self):
        """
        Test adding an artist form
        """
        form = ArtistForm({
            'name': 'another_test',
            'friendly_name': 'Another Name'
        })
        self.assertTrue(form)
