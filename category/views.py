from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from category.forms import BlogForm
from category.models import Blog, Category


# class CategoryList(ListView):
#     model = Category
#     # paginate_by = 10
#     http_method_names = ['get', ]
#     template_name = 'dashboard/index.html'
#     context_object_name = 'category'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# class CategoryCreate(CreateView, SuccessMessageMixin):
#     model = Category
#     template_name = 'category/create.html'
#     # form_class = CategoryForm
#     success_url = reverse_lazy('category:list')
#     extra_context = {'job': 'Create'}
#
#
# class CategoryUpdate(UpdateView, SuccessMessageMixin):
#     model = Category
#     template_name = 'category/update.html'
#     # form_class = CategoryForm
#     success_url = reverse_lazy('category:list')
#     extra_context = {'job': 'Update'}
#     success_message = 'Category updated successfully'
#     context_object_name = 'category'
#
#
# class CategoryDelete(DeleteView):
#     model = Category
#     success_url = reverse_lazy('category:list')


class BlogList(ListView):
    model = Blog
    # paginate_by = 10
    http_method_names = ['get', ]
    context_object_name = 'blogs'

    def get_queryset(self):
        blogs = Blog.objects.all()
        category = Category.objects.all()
        return {
            'blogs': blogs,
            'category': category,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_queryset())
        return context

    def get_template_names(self):
        path = self.request.path
        if path == reverse_lazy('dashboard'):
            return ['dashboard/index.html']
        elif path == reverse_lazy('category:blog'):
            return ['category/blog.html']
        else:
            return ['dashboard/index.html']


class BlogCreate(CreateView, SuccessMessageMixin):
    model = Blog
    template_name = 'category/add.html'
    form_class = BlogForm
    success_url = reverse_lazy('category:blog')
    success_message = "Blog was created successfully."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['job'] = 'Create'
        return context

    # def get_queryset(self):
    #     category = Category.objects.all()
    #     return {'category': category}


class BlogUpdate(UpdateView, SuccessMessageMixin):
    model = Blog
    template_name = 'category/update.html'
    form_class = BlogForm
    success_url = reverse_lazy('category:blog')
    extra_context = {'job': 'Update'}
    success_message = 'Category updated successfully'
    context_object_name = 'blog'
