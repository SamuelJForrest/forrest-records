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
    contact_form = MessageForm()

    if request.method == 'POST':
        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        }

        # Validate form - ensure no empty strings are entered
        for _, value in form_data.items():
            if not value:
                messages.error(request, 'Please ensure all required fields are completed.')
                return redirect(reverse('contact'))

        contact_form = MessageForm(form_data)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent! We\'ll be in touch soon')
        else:
            messages.error(request, 'Uh oh! Something seems to have gone wrong. Try again later.')

        return redirect(reverse('contact'))

    context = {
        'contact_page': contact_page,
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)


@login_required
def inbox(request):
    """
    Renders messages inbox
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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
            if len(inbox_items.filter(queries)) > 0:
                inbox_items = inbox_items.filter(queries)
            else:
                messages.error(request, 'Your search returned no results - please try again.')
                return redirect(reverse('inbox'))

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
