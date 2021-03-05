from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """ A view to show a product
    """

    product = get_object_or_404(Product, pk=product_id)

    template = 'products/product_detail.html'
    context = {
        'product': product
    }
    return render(request, template, context)
