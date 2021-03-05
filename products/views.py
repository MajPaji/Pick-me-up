from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def products_all(request):
    """ A view to show all the products
        and handle sorting and search queries
    """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not search any keyword')
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                    product_type__icontains=query)
            products = products.filter(queries)

    template = 'products/products.html'
    context = {
        'products': products,
        'search_keyword': query,
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
