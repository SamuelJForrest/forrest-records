from django.shortcuts import render, get_object_or_404
from .models import BlogPage, Blogs

# Create your views here.


def all_blog_posts(request):
    """
    Returns all blog posts, including sorting
    """
    blogpage = BlogPage.objects.all()
    blogs = Blogs.objects.all().order_by('-blogpage__featured_blog', '-id')

    for item in blogpage:
        if item.featured_blog is not None:
            featured_blog = item.featured_blog

    context = {
        'blogpage': blogpage,
        'blogs': blogs,
        'featured_blog': featured_blog
    }
    
    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """
    Redirects to a specific blog page
    """
    blog = get_object_or_404(Blogs, id=blog_id)
    blog_title = blog.title
    modifier = '__blogsingle'

    context = {
        'modifier': modifier,
        'blog': blog,
        'blog_title': blog_title,
    }

    return render(request, 'blog/blog-single.html', context)
