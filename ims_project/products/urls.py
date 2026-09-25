from django.urls import path
from products.views import *


urlpatterns = [
    path('', home_view),
    path('all-products/', product_view),
]