from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import ReceiptForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'There is no item in your basket!')
        return redirect(reverse('products'))

    receipt_form = ReceiptForm()
    template = 'checkout/checkout.html'
    context = {
        'receipt_form': receipt_form,
    }

    return render(request, template, context)


