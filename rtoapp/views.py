from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import *

# Create your views here.
#@login_required(login_url='login-h')
def home(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
        except:
            messages.warning("Fill the details")
        if user is not None:
            login(request, user)   
            if user.is_superuser:
                return redirect('admin-home')
            else:
                return redirect('user-home')     

            
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + username)

            return redirect('admin-user-list')
    context = {'form':form}
    return render(request, 'register.html',context)
    
def logoutUser(request):
    logout(request)
    return redirect('login')
