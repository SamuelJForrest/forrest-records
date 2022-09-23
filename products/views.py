from django.shortcuts import render
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

