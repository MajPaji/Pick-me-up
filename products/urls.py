from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_all, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<product_id>/', views.delete_product, name='delete_product'),
]
