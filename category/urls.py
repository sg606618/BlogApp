from django.urls import path
from category.views import *

app_name = 'category'

urlpatterns = [
    path('', index, name='index'),
]
