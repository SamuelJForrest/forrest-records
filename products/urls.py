from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('add_album/', views.add_album, name='add_album'),
    path('add_merch/', views.add_merch, name='add_merch'),
    path('edit_album/<album_id>', views.edit_album, name='edit_album'),
    path('edit_merch/<merch_id>', views.edit_merch, name='edit_merch'),
]
