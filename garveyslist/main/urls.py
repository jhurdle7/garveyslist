from django.urls import path 
from . import views


app_name= 'main'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:business_type>/', views.detail, name='detail'),
  path('add/', views.addbusiness, name='add_business'),
  ]
