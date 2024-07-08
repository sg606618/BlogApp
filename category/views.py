from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from category.forms import BlogForm
from category.models import Blog, Category
from account.models import Account


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


class BlogCreate(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Blog
    template_name = 'category/add.html'
    form_class = BlogForm
    success_url = reverse_lazy('category:blog')
    success_message = "Blog was created successfully."

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.added_by = Account.objects.get(id=self.request.user.id)
        blog.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['job'] = 'Create'
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('category:blog')
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['files'] = self.request.FILES
        return kwargs

class BlogUpdate(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Blog
    template_name = 'category/update.html'
    form_class = BlogForm
    success_url = reverse_lazy('category:blog')
    extra_context = {'job': 'Update'}
    success_message = 'Category updated successfully'
    context_object_name = 'blog'


class BlogView(DetailView):
    model = Blog
    template_name = 'category/blog_description.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'slug'


