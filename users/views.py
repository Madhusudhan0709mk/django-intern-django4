from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, UserLoginForm
from .models import User
from django.contrib import messages


def main_page(request):
    return render(request,'main.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"signup successfull")
            return redirect('login')
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")
            print(form.errors)
    else:
        form = UserSignupForm() 
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.success(request,"please try again")
                # If authentication fails, return the form with an error message
                return render(request, 'users/login.html', {'form': form})
    else:
       
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

   
@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html', {'user': request.user})