from django.shortcuts import render, redirect, reverse, get_object_or_404

from products.models import Product


def view_bag(request):
    """
    A view that redners the bag contents page.
    """
    page_title = 'Basket'

    context = {
        'page_title': page_title
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    digital_download = request.POST.get('digital_download')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)