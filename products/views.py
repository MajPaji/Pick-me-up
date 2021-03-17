from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm

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
            if sort_key == 'category':
                sort_key = 'category__name'

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
                    prtype__icontains=query)
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


def add_product(request):
    """ Add a product to the the web shop """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added new product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the web shop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin user can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update the product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"Editing {product.name}")

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

