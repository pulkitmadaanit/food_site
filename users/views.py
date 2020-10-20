from django.shortcuts import render,redirect, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserSignUpForm, UserLoginForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def user_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserSignUpForm()
        return render(request, 'users/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form': form})

# def register(request):
#     if request.method=="POST":
#         form= UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'welcome {username}')
            
#             return redirect('first_page')
        
#     else:        
#         form = UserCreationForm()
#         itemaa={"form":form}
#     return render(request,"users/login.html",itemaa)
