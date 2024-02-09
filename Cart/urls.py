from django.urls import path
from .import views

urlpatterns = [
    path('cart/',views.Customer_cart, name='cart'),
    path('edit_cart_items/', views.Edit_cart_items, name='edit_cart_items'),
    path('add_to_cart/', views.Add_to_cart, name='add_to_cart'),
    path('delete_order_item/', views.Delete_order_item, name='delete_order_item'),
    path('order_item_select/', views.Order_item_select, name='order_item_select'),
    path('select_all/', views.Select_all,name='select_all'),
]