from django.urls import path
from apps.order.views import add_to_cart, show_cart

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('show-cart/', show_cart, name='show_cart'),
]