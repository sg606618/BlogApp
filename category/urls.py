from django.urls import path
from category.views import *

app_name = 'category'

urlpatterns = [
    path('', BlogList.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogView.as_view(), name='blog_description'),
    path('add/', BlogCreate.as_view(), name='add'),
]
