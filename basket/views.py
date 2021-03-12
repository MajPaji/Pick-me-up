from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def basket_view(request):
    """ A view to retrun the shopping basket contents """

    template = 'basket/basket.html'
    return render(request, template)


def add_to_basket(request, item_id):
    """ Add a quantity to the product  """

    quantity = int(request.POST.get('quantity'))
    product = Product.objects.get(pk=item_id)
    current_url = request.POST.get('current_URL')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, 'One item added to your cart')
    else:
        basket[item_id] = quantity
        messages.success(request, 'One item added to your cart')

    request.session['basket'] = basket
    return redirect(current_url)


def update_basket(request, item_id):
    """ update the quantity of an item  """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('basket_view'))


def remove_basket_item(request, item_id):
    """ remove the item from shopping basket  """

    try:
        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as er:
        return HttpResponse(status=500)

