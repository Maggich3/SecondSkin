# main/urls.py

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.popular_list, name='home'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
