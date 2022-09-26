from django.shortcuts import render
from .models import Homepage


def index(request):
    """
    A view to return the index page
    """
    modifier = '__home'
    homepage = Homepage.objects.all()
    
    context = {
        'modifier': modifier,
        'homepage': homepage
    }
    return render(request, 'home/index.html', context)
