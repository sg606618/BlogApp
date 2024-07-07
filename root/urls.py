from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings

from category.views import BlogList

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('admin/', include('customadmin.urls')),

    path('__reload__/', include("django_browser_reload.urls")),

    path('blogs/', include("category.urls", namespace='category')),
    path('', BlogList.as_view(), name='dashboard'),

    path('account/', include('account.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
