from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('product_view/<int:id>', views.Product_view, name='product_view'),
]