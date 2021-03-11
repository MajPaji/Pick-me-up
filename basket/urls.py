from django.urls import path
from . import views


urlpatterns = [
    path('', views.basket_view, name='basket_view'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('update/<item_id>/', views.update_basket, name='update_basket'),
    path('remove/<item_id>/', views.remove_basket_item, name='remove_basket_item'),
]
