from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as auth_logout
from .forms import SignUpForm, SignInForm


def redirect_if_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)

    return wrapper


@redirect_if_authenticated
def signup(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('account:login')
    else:
        form = SignUpForm()
    return render(req, 'account/register.html', {'form': form})


@redirect_if_authenticated
def signin(req):
    if req.method == 'POST':
        form = SignInForm(req, req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('dashboard')
    else:
        form = SignInForm()
    return render(req, 'account/login.html', {'form': form})


@login_required
def logout(req):
    if req.method == 'POST':
        auth_logout(req)
        return redirect('account:login')
    return redirect('dashboard')
