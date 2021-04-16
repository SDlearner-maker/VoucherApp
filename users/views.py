from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserRegisterForm

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

