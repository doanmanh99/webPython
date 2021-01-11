from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index),
    path('sanpham/', views.sanpham),
    path('sanpham/<int:id>', views.danhmucsp),
    path('detail/<int:id>', views.detail),
    path('contact/', views.contact),
    path('cart/', views.viewcart),
    path('sanpham/addCart', views.addCart,name='addcart'),
    path('detail/addCart', views.addCart,name='addcart')
]