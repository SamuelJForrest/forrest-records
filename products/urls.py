from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('add/album/', views.add_album, name='add_album'),
    path('add/merch/', views.add_merch, name='add_merch'),
    path('edit/album/<album_id>', views.edit_album, name='edit_album'),
    path('edit/merch/<merch_id>', views.edit_merch, name='edit_merch'),
    path('album/warning/<album_id>', views.album_warning, name='album_warning'),
    path('delete/album/<album_id>', views.delete_album, name='delete_album'),
    path('merch/warning/<merch_id>', views.merch_warning, name='merch_warning'),
    path('delete/merch/<merch_id>', views.delete_merch, name='delete_merch'),
]
