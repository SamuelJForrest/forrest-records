from django.shortcuts import render

# Create your views here.

def contact_us(request):
    """
    Renders the contact page, and handles the form submission
    """
    page_title = "Contact"
    page_description = "Get in touch"

    context = {
        'page_title': page_title,
        'page_description': page_description
    }

    return render(request, 'contact/contact.html', context)
