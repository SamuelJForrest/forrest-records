from django.test import TestCase
from django.urls import reverse, resolve
from .views import checkout, checkout_success
from .models import Order, OrderLineItem
from .forms import OrderForm

# Model tests

class TestOrderModels(TestCase):
    """
    Test order models
    """
    def test_create_order(self):
        """
        Create a test order model
        """
        model = Order.objects.create(
            order_number=400,
            full_name='full name',
            email='email@email.com',
            phone_number='0123456789',
            country='United Kingdom',
            town_or_city='Cardiff',
            address1='address',
            delivery_cost=13,
            order_total=100,
            grand_total=113,
            original_bag='bag',
            stripe_pid='example-pid'
        )
        self.assertTrue([
            model.order_number,
            model.full_name,
            model.email,
            model.phone_number,
            model.country,
            model.town_or_city,
            model.address1,
            model.delivery_cost,
            model.order_total,
            model.grand_total,
            model.original_bag,
            model.stripe_pid
        ])  

# views tests

class TestCheckoutUrls(TestCase):
    """
    Test Checkout URLs
    """

    def test_checkout_url(self):
        """
        Test checkout url returns 200
        """
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_checkout_success_url(self):
        """
        Test checkout success
        """
        url = reverse('checkout_success', args=[1])
        self.assertTrue(resolve(url).func, checkout_success)


# Form test
class TestOrderForm(TestCase):
    """
    Test Order form
    """

    def test_order_form(self):
        """
        Test creating order form
        """
        form = OrderForm({
            'order_number': 400,
            'full_name': 'full name',
            'email': 'email@email.com',
            'phone_number': '0123456789',
            'country': 'United Kingdom',
            'town_or_city': 'Cardiff',
            'address1': 'address',
            'delivery_cost': 13,
            'order_total': 100,
            'grand_total': 113,
            'original_bag': 'bag',
            'stripe_pid': 'example-pid'
        })
        self.assertTrue(form)
