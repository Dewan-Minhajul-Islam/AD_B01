from django.shortcuts import render

# Create your views here.
def employee_view(request):
    
    return render(request, 'employee.html')