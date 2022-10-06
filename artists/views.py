from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Artist

from .models import Artist
from .forms import ArtistForm

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


@login_required
def add_artist(request):
    """
    Adds a new artist to the artist page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('artists'))

    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            messages.success(request, 'Successfully added artist!')
            return redirect(reverse('artists'))
        else:
            messages.error(request, 'Failed to add artist.')
    else:
        form = ArtistForm()

    page_title = 'Add artist'
    template = 'artists/add-artist.html'
    context = {
        'page_title': page_title,
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_artist(request, artist_id):
    """
    Renders edit artist form, and updates artist model
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('artists'))

    page_title = 'Edit Artist'
    artist = get_object_or_404(Artist, pk=artist_id)

    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully edited {artist.name}')
            return redirect(reverse('artists'))
        else:
            messages.error(request, 'Failed to add product. ')
    else:
        form = ArtistForm(instance=artist)
        messages.info(request, f'You are editing {artist.name}')

    template = 'artists/edit-artist.html'
    context = {
        'page_title': page_title,
        'form': form,
    }

    return render(request, template, context)

