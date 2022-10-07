from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order/history/<order_number>',
        views.order_history,
        name='order_history'
    ),
    path(
        'add/wishlist/<item_id>',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),
    path(
        'remove/wishlist/<item_id>',
        views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),
    path('all/', views.all_profiles, name='all_profiles')
]
