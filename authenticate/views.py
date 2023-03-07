from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'authenticate/home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:

            return redirect('home')
    else:
        return render(request, 'authenticate/home.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form1 = SignUpForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data['username']
            password = form1.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form1 = SignUpForm(request.POST)
    else:
        form1 = SignUpForm()
    context = {
        'form1': form1,
    }
    return render(request, 'authenticate/register.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'authenticate/edit_profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
        print(form)
    context = {
        'form': form,
    }
    return render(request, 'authenticate/change_password.html', context)
