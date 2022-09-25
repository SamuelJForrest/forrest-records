from django.shortcuts import render
from .models import Artist

# Create your views here.

def all_artists(request):
    """
    Returns the page that displays all artists
    """
    
    page_title = 'Artists'
    artists = Artist.objects.all().order_by('name')

    context = {
        'page_title': page_title,
        'artists': artists,
    }

    return render(request, 'artists/artists.html', context)