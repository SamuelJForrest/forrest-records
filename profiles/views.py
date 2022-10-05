from django.shortcuts import render

# Create your views here.


def profile(request):
    """
    Renders profile page
    """
    page_title = 'My Profile'

    context = {
        'page_title': page_title
    }

    return render(request, 'profiles/profile.html', context)
