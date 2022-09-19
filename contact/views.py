from django.shortcuts import render

# Create your views here.

def contact_us(request):
    """
    Renders the contact page, and handles the form submission
    """
    page_title = "Contact"

    context = {
        'page_title': page_title
    }

    return render(request, 'contact/contact.html', context)
