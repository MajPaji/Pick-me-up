from django.shortcuts import render
from .models import Product

# Create your views here.


def products_all(request):
    """ A view to show all the products
        and handle sorting and search queries
    """

    products = Product.objects.all()

    template = 'products/products.html'
    context = {
        'products': products
    }
    return render(request, template, context)
