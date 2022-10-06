from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('<blog_id>', views.blog_detail, name='blog_detail'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<blog_id>', views.edit_blog, name='edit_blog'),
    path('delete_blog/<blog_id>', views.delete_blog, name='delete_blog'),
    path('blog_warning/<blog_id>', views.blog_warning, name='blog_warning'),
]
