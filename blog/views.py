from django.shortcuts import render

# Create your views here.


def all_blog_posts(request):
    """
    Returns all blog posts, including sorting
    """
    page_title = 'Blog'
    page_description = 'All of our latest news'

    context = {
        'page_title': page_title,
        'page_description': page_description
    }
    
    return render(request, 'blog/blog.html', context)
