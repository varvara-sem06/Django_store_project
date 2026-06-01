from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/create/', views.product_create, name='product_create')
]
