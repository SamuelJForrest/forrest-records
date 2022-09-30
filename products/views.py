from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Album, Song
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

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
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

    digital_download_enabled = False

    if request.GET:
        if 'format' in request.GET:
            format = request.GET['format']
            if format == 'digital_download':
                digital_download_enabled = True

    context = {
        'product': product,
        'product_name': product_name,
        'related_products': related_products,
        'digital_download_enabled': digital_download_enabled,
    }

    return render(request, 'products/products-single.html', context)
