from django.urls import path
from category.views import *

app_name = 'category'

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('news/', news, name='news'),
]
