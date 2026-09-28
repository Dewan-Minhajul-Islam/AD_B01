from django.urls import path
from users.views import *


urlpatterns = [
    path('', login_view, name='login_page'),
    path('register/', register_view, name='register_page')
]
