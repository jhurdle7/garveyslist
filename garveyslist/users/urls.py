from django.urls import path 
from . import views


app_name= 'users'
urlpatterns = [
    path('username/', views.user, name='user'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_user, name='logout_user'),
    
  ]
