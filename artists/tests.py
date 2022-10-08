from django.test import TestCase
from .models import Artist
from .forms import ArtistForm


class TestArtistViews(TestCase):
    """
    Tests artist views
    """

    def test_get_artist_page(self):
        response = self.client.get('/artists')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artists/artists.html')

    # def test_get_add_artist_page(self):

    # def test_get_edit_artist_page(self):
    
    # def test_can_add_artist(self):

    # def test_can_delete_artist

class TestArtistModels(TestCase):
    """
    Tests the artist models
    """

    def test_create_artist_models(self):
        """
        Create test artist model
        """
        Artist.objects.create(
            name='testing',
            friendly_name='Testing'
        )

class TestArtistForm(TestCase):
    """
    Tests for artist form
    """

    def test_artist_name_is_required(self):
        form = ArtistForm({'name': ''})
        self.assertFalse(form.is_valid())
    
    def test_artist_friendly_name_is_required(self):
        form = ArtistForm({'friendly_name': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ArtistForm()
        self.assertEqual(form.Meta.fields, '__all__')
