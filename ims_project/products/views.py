from django.shortcuts import render, redirect
from products.models import ProductModel

# Create your views here.
def home_view(request):
    
    return render(request, 'home.html')


def product_view(request):
    
    pr_data = ProductModel.objects.all()
    
    context = {
        'p_data' : pr_data
    }
    
    return render(request, 'product-list.html', context)


def product_form(request):
    
    if request.method == 'POST':
        
        vp_name = request.POST.get('p_name')
        vp_description = request.POST.get('p_description')
        vp_date = request.POST.get('p_date')
        vp_type = request.POST.get('p_type')
        vp_image = request.FILES.get('p_image')
        
        ProductModel.objects.create(
            product_name = vp_name,
            description = vp_description,
            production_date = vp_date,
            product_type = vp_type,
            image = vp_image
        )
        
        return redirect('products_page')
    
    return render(request, 'add-product.html')