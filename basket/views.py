from django.shortcuts import render, redirect

# Create your views here.


def basket_view(request):
    """ A view to retrun the shopping basket contents """

    template = 'basket/basket.html'
    return render(request, template)


def add_to_basket(request, item_id):
    """ Add a quantity to the product  """

    quantity = int(request.POST.get('quantity'))
    current_url = request.POST.get('current_URL')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    
    return redirect(current_url)
