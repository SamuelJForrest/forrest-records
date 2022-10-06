from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_artists, name='artists'),
    path('add_artist', views.add_artist, name='add_artist'),
    path('edit_artist/<artist_id>', views.edit_artist, name='edit_artist'),
]
