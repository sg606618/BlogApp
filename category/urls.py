from django.urls import path
from category.views import *

app_name = 'category'

urlpatterns = [
    path('blog/', BlogList.as_view(), name='blog'),
    path('add/', BlogCreate.as_view(), name='add'),
]
