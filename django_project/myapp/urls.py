from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.user_list, name='user_list'),
    path('users/<str:email>/', views.users_by_email, name='users_by_email'),
    path('users/exclude/<str:username>/', views.users_by_exclude_username, name='users_by_username'),
    path('users/<int:id>/', views.users_by_id, name='users_by_id'),
    
]


