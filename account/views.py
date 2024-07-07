# From Django Contrib Packages
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

# View Functions and Classes
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user=user)
                messages.success(request, "Successfully Logged In.")
                return redirect('category:list')
            else:
                messages.error("Inactive user cannot login")
                return redirect('account:login')
        else:
            messages.error(request, "User name and password did not match")
            return redirect('account:login')


class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account:login')

    def get(self, request):
        logout(request)
        return redirect('account:login')
