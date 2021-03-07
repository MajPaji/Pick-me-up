from django.conf import settings
from decimal import Decimal

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0

    total_plus_tax = total + Decimal(total * settings.TAX_PERCENTAGE / 100)

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'total_plus_tax': total_plus_tax,
    }

    return context