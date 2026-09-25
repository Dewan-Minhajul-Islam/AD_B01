from django.urls import path
from products.views import *


urlpatterns = [
    path('', home_view, name='home_page'),
    path('all-products/', product_view, name='products_page'),
    path('add-product/', product_form, name='add_product_page'),
]