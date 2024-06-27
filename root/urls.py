from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include("django_browser_reload.urls")),
    path('category/', include("category.urls")),
    path('', TemplateView.as_view(template_name='dashboard/index.html'), name='dashboard'),
]
