from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .forms import ReceiptForm, Receipt
from basket.contexts import basket_contents
from .models import ReceiptLineItem
from products.models import Product
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address': request.POST['street_address'],
        }
        receipt_form = ReceiptForm(form_data)
        if receipt_form.is_valid():
            receipt = receipt_form.save()
            for item_id, quantity in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    receipt_line_item = ReceiptLineItem(
                        receipt=receipt,
                        product=product,
                        quantity=quantity,
                    )
                    receipt_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    receipt.delete()
                    return redirect(reverse('basket_view'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[receipt.receipt_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please check your detail information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'There is no item in your basket!')
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total_plus_tax = current_basket['total_plus_tax']
        stripe_total_plus_tax = round(total_plus_tax * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total_plus_tax,
            currency=settings.STRIPE_CURRENCY,
        )

        receipt_form = ReceiptForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Check your setting environment?')

    template = 'checkout/checkout.html'
    context = {
        'receipt_form': receipt_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, receipt_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')

    receipt = get_object_or_404(Receipt, receipt_number=receipt_number)

    messages.success(request, f'Order successfully processed! \
        Your receipt number is {receipt_number}. A confirmation \
        email will be sent to your email at: {receipt.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'receipt': receipt,
    }

    return render(request, template, context)
