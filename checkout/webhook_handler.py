from django.http import HttpResponse

from .models import Receipt, ReceiptLineItem
from products.models import Product


import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        total_plus_tax = round(intent.charges.data[0].amount / 100, 2)

        # remove empty data in shipping detail
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        receipt_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                receipt = Receipt.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address__iexact=shipping_details.address.line1,
                    total_plus_tax=total_plus_tax,
                    original_basket=basket,
                    stripe_pid=pid,
                )

                receipt_exists = True
                break
            except Receipt.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if receipt_exists:
            return HttpResponse(content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database ', status=200)
        else:
            receipt = None
            try:
                receipt = Receipt.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address=shipping_details.address.line1,
                    original_basket=basket,
                    stripe_pid=pid,
                )

                for item_id, quantity in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    receipt_line_item = ReceiptLineItem(
                        receipt=receipt,
                        product=product,
                        quantity=quantity,
                    )
                    receipt_line_item.save()
            except Exception as e:
                if receipt:
                    receipt.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

