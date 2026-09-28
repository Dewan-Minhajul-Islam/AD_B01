from django.shortcuts import render, redirect
from users.models import CustomUserModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_view(request):
    
    if request.method == 'POST':
        
        ru_name = request.POST.get('u_name')
        ru_email = request.POST.get('u_email')
        ru_f_name = request.POST.get('u_f_name')
        ru_l_name = request.POST.get('u_l_name')
        ru_type = request.POST.get('u_type')
        ru_image = request.FILES.get('u_image')
        ru_password = request.POST.get('u_password')
        ru_conf_password = request.POST.get('u_conf_password')
        
        if ru_password == ru_conf_password:
            
            CustomUserModel.objects.create_user(
                username = ru_name,
                email = ru_email,
                first_name = ru_f_name,
                last_name = ru_l_name,
                user_type = ru_type,
                image = ru_image,
                password = ru_password
            )
            
            return redirect('login_page')
        else:
            print('Passwords didn`t matched')
            
    
    return render(request, 'register.html')


def login_view(request):
    
    if request.method == 'POST':
        
        lu_name = request.POST.get('u_name')
        lu_password = request.POST.get('u_password')
        
        log_user = authenticate(
            request,
            username = lu_name,
            password = lu_password
        )
        
        if log_user:
            login(request, log_user)
            return redirect('home_page')
        else:
            print('Invalid Username or Password!')
    
    return render(request, 'login.html')


@login_required
def logout_view(request):
    
    logout(request)
    
    return redirect('login_page')