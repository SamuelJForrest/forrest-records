from django.shortcuts import render, get_object_or_404
from .models import Product, Album, Song

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """
    page_title = 'Shop'
    products = Product.objects.all()
    albums = Album.objects.all()

    context = {
        'page_title': page_title,
        'products': products,
        'albums': albums
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Redirects to individual product page
    """

    product = get_object_or_404(Product, id=product_id)
    product_name = product.name

    context = {
        'product': product,
        'product_name': product_name
    }

    return render(request, 'products/products-single.html', context)
