from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_all, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
