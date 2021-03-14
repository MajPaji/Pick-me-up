from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('wh/', webhook, name='webhook'),
    path('', views.checkout, name='checkout'),
    path('checkout_success/<receipt_number>',
         views.checkout_success, name='checkout_success'),
]
