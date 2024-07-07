from django.urls import path
from customadmin import views

app_name = 'customadmin'

urlpatterns = [
    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),

    path('update/<slug:slug>', views.category_update, name='update'),
    path('delete/<slug:slug>', views.category_delete, name='delete'),

    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('blog/', views.blog, name='blog'),

    path('category/', views.category, name='category'),
    path('category/add/', views.add_category, name='add'),
]
