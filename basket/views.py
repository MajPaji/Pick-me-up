from django.shortcuts import render

# Create your views here.


def basket_view(request):
    """ A view to retrun the shopping basket contents """

    template = 'basket/basket.html'
    return render(request, template)

