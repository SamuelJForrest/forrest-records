from django.shortcuts import render, get_object_or_404
from .models import Product, Album, Song

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    page_title = 'Shop'
    products = Product.objects.all()
    product_type = None

    if request.GET:
        if 'product_type' in request.GET:
            product_type = request.GET['product_type'].split(',')
            if 'album' in product_type:
                page_title = 'Albums'
            elif 'merch' in product_type:
                page_title = 'Merchandise'
            products = products.filter(product_type__name__in=product_type)


    context = {
        'page_title': page_title,
        'products': products,
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
