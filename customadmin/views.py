from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from category.models import Blog, Category
from customadmin.forms import CategoryForm


@login_required(login_url='customadmin:login')
def index(req):
    category = Category.objects.all()
    blogs = Blog.objects.all()
    blog_count = blogs.count()
    return render(req, 'customadmin/dashboard.html', {'blog_count': blog_count, 'category_count': category.count()})


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
    return render(req, 'customadmin/users.html')


def admin_login(req):
    try:
        if req.user.is_authenticated:
            return redirect('customadmin:index')

        if req.method == 'POST':
            username = req.POST['username']
            password = req.POST['password']

            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(req, "Account not found!!!")
                return HttpResponseRedirect(req.META.get('HTTP_REFERER', '/'))

            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(req, user_obj)
                return redirect('customadmin:index')

            messages.info(req, "Invalid username or password")
            return redirect('customadmin:login')
        return render(req, 'customadmin/login.html')
    except Exception as e:
        print(e)
        return render(req, 'customadmin/login.html')


def admin_logout(req):
    logout(req)
    return redirect('customadmin:login')


def category_delete(req, slug):
    cat = get_object_or_404(Category, slug=slug)
    cat.delete()
    messages.success(req, 'Category deleted successfully.')
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
