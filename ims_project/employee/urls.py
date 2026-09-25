from django.urls import path
from employee.views import employee_view


urlpatterns = [
    path('employee/', employee_view, name='employee_page'),
]
