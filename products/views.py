from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def products_all(request):
    """ A view to show all the products
        and handle sorting and search queries
    """

    products = Product.objects.all()
    query = None
    categories = None
    prtype = None
    sort = None
    direction = None

    if request.GET:
        if 'prtype' in request.GET:
            prtype = request.GET['prtype']
            products = products.filter(prtype__in=[f'{prtype}'])

        if 'sort' in request.GET:
            sort = request.GET['sort']
            sort_key = sort
            if sort_key == 'name':
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not search any keyword')
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(
                    product_type__icontains=query)
            products = products.filter(queries)
    current_sorting = f'{prtype}_{sort}_{direction}'

    template = 'products/products.html'
    context = {
        'products': products,
        'search_keyword': query,
        'filter_categories': categories,
        'selected_bean': prtype,
        'current_sorting': current_sorting,
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
