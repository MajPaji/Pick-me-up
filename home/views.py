from django.shortcuts import render

# Create your views here.


def error_404(request):
    return render(request, '404.html')


def home(request):
    """ A view to retrun the home page """

    return render(request, 'home/home.html')
