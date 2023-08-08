from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.

def signIn(request):
    return render (request, 'accounts/signin.html', context= {} )


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully Registered!")
            #authenticate and log in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Sign in here!")
            return redirect('sign-in')
    else:
        form = RegisterForm()
        context = {'form': form}
        return render (request, 'accounts/register.html', context )
    context = {'form': form}
    return render (request, 'accounts/register.html', context )


def registerSchool(request):
    return render (request, 'accounts/register-sch.html', context= {} )
