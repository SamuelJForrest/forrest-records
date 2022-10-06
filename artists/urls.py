from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artists, name='artists'),
    path('add/artist', views.add_artist, name='add_artist'),
    path('edit/artist/<artist_id>', views.edit_artist, name='edit_artist'),
    path('artist/warning/<artist_id>', views.artist_warning, name='artist_warning'),
    path('delete/artist/<artist_id>', views.delete_artist, name='delete_artist'),
]
