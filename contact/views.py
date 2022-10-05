from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import ContactPage, Message
from .forms import MessageForm


def contact_us(request):
    """
    Renders the contact page, and handles the form submission
    """
    contact_page = ContactPage.objects.all()
    contact_form = MessageForm(request.POST)

    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save(request.POST)
            messages.success(request, 'Your message has been sent! We\'ll be in touch soon')
        else:
            messages.error(request, 'Uh oh! Something seems to have gone wrong. Try again later.')

        return redirect(reverse('contact'))

    context = {
        'contact_page': contact_page,
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)


def inbox(request):
    """
    Renders messages inbox
    """

    inbox_items = Message.objects.all()

    if request.GET:
        if 'message-search' in request.GET:
            query = request.GET['message-search']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                )
                return redirect(reverse('inbox'))

            queries = Q(
                name__icontains=query) | Q(
                    message__icontains=query)
            inbox_items = inbox_items.filter(queries)


    template = 'contact/inbox.html'
    context = {
        'inbox_items': inbox_items,
    }

    return render(request, template, context)


def view_single_message(request, message_id):
    """
    Renders Template for individual messages
    """

    inbox_item = get_object_or_404(Message, pk=message_id)
    template = 'contact/inbox-message.html'
    context = {
        'inbox_item': inbox_item
    }

    return render(request, template, context)
