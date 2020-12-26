from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationFom
from shop.models import Cart
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationFom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            Cart.objects.create(user = User.objects.get(username = username))
            return redirect('login')
    else:
        form = UserRegistrationFom()
    return render(request, 'users/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')