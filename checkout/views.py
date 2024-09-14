from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Pyc4YRuJYd0ybghKYzwJZxOSsk1TVyl23x4VTJmro4GWu5nLeoMUDcY2pD5v9xhcziCnSMfeXAStXA5iJkcy4Up00woGqXbFb',
        'client_serect': 'test client serect',
    }

    return render(request, template, context)
