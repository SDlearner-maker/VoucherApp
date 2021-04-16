from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account\'s password has been changed, you can now Log In with the new password')
            return redirect('voucher-homepage')
    else:
        form = PasswordChangeForm(request.user)   
    
    return render(request, 'users/register.htm', {'form': form})

def log_in(request): 
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            messages.warning(request, 'Don\'t forget to change your password if this is your first time login')
            login(request, user)
            return redirect('voucher-homepage')
    else:
        form = AuthenticationForm()   
    
    return render(request, 'users/login.htm', {'form': form})

