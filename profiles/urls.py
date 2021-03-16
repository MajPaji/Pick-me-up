from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('receipt_history/<receipt_number>', views.receipt_history, name='receipt_history'),
]
