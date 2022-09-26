from django.shortcuts import render
from .models import ContactPage


def contact_us(request):
    """
    Renders the contact page, and handles the form submission
    """
    contact_page = ContactPage.objects.all()

    context = {
        'contact_page': contact_page
    }

    return render(request, 'contact/contact.html', context)
