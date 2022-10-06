from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Album, Song, Merch
from .forms import AlbumForm, MerchForm
from artists.models import Artist


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    page_title = 'Shop'
    products = Product.objects.all()
    product_type = None
    artist = None
    sort = None
    direction = None
    query = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'artist':
                sortkey = 'artist__name'
            if sortkey == 'sale':
                sortkey = 'on_sale'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'product_type' in request.GET:
            product_type = request.GET['product_type'].split(',')
            if 'album' in product_type:
                page_title = 'Albums'
            elif 'merch' in product_type:
                page_title = 'Merchandise'
            products = products.filter(product_type__name__in=product_type)

        if 'artist' in request.GET:
            artist = request.GET['artist']
            products = products.filter(artist__name__contains=artist)
            artist_set = Artist.objects.filter(name__contains=artist)
            for item in artist_set:
                page_title = item.friendly_name

        # search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                        name__icontains=query) | Q(
                        description__icontains=query)
            products = products.filter(queries)
                
    current_sorting = f'{sort}_{direction}'

    context = {
        'page_title': page_title,
        'product_type': product_type,
        'products': products,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Redirects to individual product page
    """

    product = get_object_or_404(Product, id=product_id)
    product_name = product.name
    related_products = Product.objects.filter(
                       artist=product.artist).exclude(
                       id=product_id)[:4]

    context = {
        'product': product,
        'product_name': product_name,
        'related_products': related_products,
    }

    return render(request, 'products/products-single.html', context)


@login_required
def add_album(request):
    """
    Add an album to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    page_title = 'Add Album'
    album = True

    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. ')
    else:
        form = AlbumForm()

    template = 'products/add_product.html'
    context = {
        'page_title': page_title,
        'form': form,
        'album': album,
    }

    return render(request, template, context)


@login_required
def add_merch(request):
    """
    Add merch to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    page_title = 'Add Merch'
    merch = True

    if request.method == 'POST':
        form = MerchForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = MerchForm()

    template = 'products/add_product.html'
    context = {
        'page_title': page_title,
        'form': form,
        'merch': merch,
    }

    return render(request, template, context)


@login_required
def edit_album(request, album_id):
    """
    Edit an album in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    page_title = 'Edit Album'
    album = get_object_or_404(Album, pk=album_id)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully edited {album.name}')
            return redirect(reverse('product_detail', args=[album.id]))
        else:
            messages.error(request, 'Failed to add product. ')
    else:
        form = AlbumForm(instance=album)
        messages.info(request, f'You are editing {album.name}')

    template = 'products/edit_product.html'
    context = {
        'page_title': page_title,
        'form': form,
        'album': album
    }

    return render(request, template, context)


@login_required
def edit_merch(request, merch_id):
    """
    Edit merch in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    page_title = 'Edit Merch'
    merch = get_object_or_404(Merch, pk=merch_id)

    if request.method == 'POST':
        form = MerchForm(request.POST, instance=merch)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully edited "{merch.name}"')
            return redirect(reverse('product_detail', args=[merch.id]))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = MerchForm(instance=merch)
        messages.info(request, f'You are editing "{merch.name}"')

    template = 'products/edit_product.html'
    context = {
        'page_title': page_title,
        'form': form,
        'merch': merch
    }

    return render(request, template, context)
