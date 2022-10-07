from django.http import Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product
from profiles.models import UserProfile, Wishlist


def profile(request):
    """
    Renders profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, pk=request.user.id)
        try:
            wishlist = get_object_or_404(Wishlist, created_by=user.id)
        except Http404:
            wishlist = None
    else:
        wishlist = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'wishlist': wishlist,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout-success.html'
    page_title = 'Past Order'
    context = {
        'page_title': page_title,
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, item_id):
    """
    Add a product to user's wishlist
    """

    product = get_object_or_404(Product, pk=item_id)
    user = get_object_or_404(UserProfile, pk=request.user.id)

    try:
        wishlist = get_object_or_404(Wishlist, created_by=user.id)
    except Http404:
        wishlist = Wishlist.objects.create(created_by=user)

    if product in wishlist.products.all():
        messages.info(request, 'This product is already in your wishlist')
    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.name} has been added to your wishlist')

    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def remove_from_wishlist(request, item_id):
    """
    Remove a product from user's wishlist
    """

    product = get_object_or_404(Product, pk=item_id)
    user = get_object_or_404(UserProfile, pk=request.user.id)
    wishlist = get_object_or_404(Wishlist, created_by=user.id)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f'{product.name} has been removed from your wishlist')
    else:
        messages.error(request, 'That product is not in your favourites')

    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def all_profiles(request):
    """
    Renders all profiles
    """
    if not request.user.is_staff:
        messages.error(request, 'This page is for staff only.')
        return redirect(reverse('home'))

    profiles = UserProfile.objects.all()

    template = 'profiles/all-profiles.html'
    context = {
        'profiles': profiles
    }

    return render(request, template, context)
