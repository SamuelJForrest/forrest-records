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
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('artists'))

    if request.method == 'POST':

        # Form validation - extra check against empty fields
        required_fields = {
            'name': request.POST['name'],
            'friendly_name': request.POST['friendly_name'],
        }

        for _, value in required_fields.items():
            if not value:
                messages.error(request, 'Please ensure all required fields are completed.')
                return redirect(reverse('add_artist'))

        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
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
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('artists'))

    page_title = 'Edit Artist'
    artist = get_object_or_404(Artist, pk=artist_id)

    if request.method == 'POST':

        # Form validation - extra check against empty fields
        required_fields = {
            'name': request.POST['name'],
            'friendly_name': request.POST['friendly_name'],
        }

        for _, value in required_fields.items():
            if not value:
                messages.error(request, 'Please ensure all required fields are completed.')
                return redirect(reverse('edit_artist', args=[artist.id]))
        
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully edited {artist.friendly_name}')
            return redirect(reverse('edit_artist', args=[artist.id]))
        else:
            messages.error(request, 'Failed to add product. ')
    else:
        form = ArtistForm(instance=artist)
        messages.info(request, f'You are editing {artist.friendly_name}')

    template = 'artists/edit-artist.html'
    context = {
        'page_title': page_title,
        'form': form,
        'artist': artist,
    }

    return render(request, template, context)


@login_required
def artist_warning(request, artist_id):
    """
    Renders the warning page before a store owner deletes an artist
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('artists'))

    page_title = 'Warning!'
    artist = get_object_or_404(Artist, pk=artist_id)
    template = 'includes/warning/warning.html'
    context = {
        'page_title': page_title,
        'artist': artist
    }

    return render(request, template, context)


@login_required
def delete_artist(request, artist_id):
    """
    Delete an artist
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    artist.delete()
    messages.success(request, f'{artist.friendly_name} has been deleted!')
    return redirect(reverse('artists'))
