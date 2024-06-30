from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def admin_login(req):
    try:
        if req.user.is_authenticated:
            return redirect('dashboard')
        if req.method == 'POST':
            username = req.POST['username']
            password = req.POST['password']
            user_obj = User.objects.filter(username=username, password=password)
            if not user_obj.exists():
                messages.info(req, "Account not found!!!")
                return HttpResponseRedirect(req.META.get['HTTP_REFERER'])

            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(req, user_obj)
                return redirect('dashboard')

            messages.info(req, "Invalid username or password")
            return redirect('dashboard')
        return render(req, 'login')
    except Exception as e:
        print(e)

