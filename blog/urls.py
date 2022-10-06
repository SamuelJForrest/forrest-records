from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('<blog_id>', views.blog_detail, name='blog_detail'),
    path('add/blog/', views.add_blog, name='add_blog'),
    path('edit/blog/<blog_id>', views.edit_blog, name='edit_blog'),
    path('delete/blog/<blog_id>', views.delete_blog, name='delete_blog'),
    path('feature/blog/<blog_id>', views.feature_blog, name='feature_blog'),
    path('blog/warning/<blog_id>', views.blog_warning, name='blog_warning'),
]
