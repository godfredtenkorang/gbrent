from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegisterForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signUp')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect("index")
            
    context = {
        'form': form,
        'title': "Login"
    }
    return render(request, 'accounts/login.html', context)

# logout
def logout(request):
    auth.logout(request)
    
    return redirect('login')

def dashboardHome(request):
    return render(request, 'dashboard/dashboardHome.html')

def schedule(request):
    return render(request, 'dashboard/schedule.html')

def wishListPage(request):
    return render(request, 'dashboard/wishListPage.html')

def help(request):
    return render(request, 'dashboard/help.html')

def account(request):
    return render(request, 'dashboard/account.html')

def userDashboard(request):
    return render(request, 'dashboard/userDashboard.html')
