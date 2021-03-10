from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal
from products.models import Product

def basket_contents(request):

    basket_items = []
    total_cost = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, qty in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total_cost += qty * product.price
        product_count += qty
        basket_items.append({
            'item_id': item_id,
            'qty': qty,
            'product': product,
        })

    total_plus_tax = total_cost + Decimal(total_cost * settings.TAX_PERCENTAGE / 100)

    context = {
        'basket_items': basket_items,
        'total_cost': total_cost,
        'product_count': product_count,
        'total_plus_tax': total_plus_tax,
        'TAX_PERCENTAGE': settings.TAX_PERCENTAGE,
    }
    return context