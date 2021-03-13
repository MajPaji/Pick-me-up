from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<receipt_number>', views.checkout_success, name='checkout_success'),
]
