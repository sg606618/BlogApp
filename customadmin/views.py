from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from account.models import Account
from category.models import Blog, Category
from .forms import CategoryForm


@login_required(login_url='customadmin:login')
def index(req):
    cat = Category.objects.all()
    blogs = Blog.objects.all()
    account = Account.objects.all()
    return render(req, 'customadmin/dashboard.html',
                  {'blog_count': blogs.count(), 'category_count': cat.count(), 'account_count': account.count()})


@login_required(login_url='customadmin:login')
def blog(req):
    blogs = Blog.objects.all()
    return render(req, 'customadmin/blogs.html', {'blogs': blogs})


@login_required(login_url='customadmin:login')
def category(req):
    cat = Category.objects.all()
    return render(req, 'customadmin/category.html', {'category': cat})


@login_required(login_url='customadmin:login')
def user(req):
    account = Account.objects.all()
    return render(req, 'customadmin/users.html', {'account': account})


def admin_login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(req, "Account not found!!!")
            return redirect('customadmin:login')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('customadmin:index')
        else:
            messages.error(req, "Invalid username or password")
            return redirect('customadmin:login')

    return render(req, 'customadmin/login.html')


def admin_logout(req):
    logout(req)
    return redirect('customadmin:login')


def category_delete(req, slug):
    try:
        cat = get_object_or_404(Category, slug=slug)
        cat.delete()
        messages.success(req, 'Category deleted successfully.')
    except Exception as e:
        messages.error(req, 'Cannot delete the category because it is referenced by some blogs.', e)
    return redirect('customadmin:category')


def category_update(req, slug):
    try:
        if slug is None:
            messages.error(req, 'Invalid category slug.')
            return redirect('customadmin:category')

        cat = get_object_or_404(Category, slug=slug)

        if req.method == 'POST':
            form = CategoryForm(req.POST, instance=cat)
            if form.is_valid():
                form.save()
                messages.success(req, 'Category updated successfully.')
                return redirect('customadmin:category')
        else:
            form = CategoryForm(instance=cat)
        return render(req, 'customadmin/category_form.html', {'form': form, 'category': cat})

    except Category.DoesNotExist:
        messages.error(req, 'Category does not exist.')
        return redirect('customadmin:category')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save()
            return redirect('customadmin:category')
    else:
        form = CategoryForm()
    return render(request, 'customadmin/add_category.html', {'form': form})
