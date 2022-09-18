from django.shortcuts import render

# Create your views here.

def index(request):
    """
    A view to return the index page
    """
    modifier = '__home'
    
    context = {
        'modifier': modifier
    }
    return render(request, 'home/index.html', context)
