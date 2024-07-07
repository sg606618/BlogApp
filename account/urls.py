from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('login/', signin, name='login'),
    path('register/', signup, name='register'),
    path('logout/', logout, name='logout'),
]
