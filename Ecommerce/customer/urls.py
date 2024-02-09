from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('product_view/<int:id>/<str:category>/<str:name>', views.Product_view, name='product_view'),
    path('search_product/', views.Search_product, name='search_products'),
    path('order_history/', views.Orders_history, name='order_history'),
    path('cart/', views.Customer_cart, name='customer_cart'),
    path('add_to_cart/<int:id>', views.Add_to_cart,name='add_to_cart'),
    path('select_all/<int:id>', views.Select_all,name='select_all'),
    path('edit_order_items/<int:id>', views.Edit_order_items, name='edit_order_items'),
    path('order_item_delete/<int:id>', views.Order_item_delete, name='order_item_delete'),
    path('order_checkout/', views.Order_checkout, name='order_checkout'),
    path('buy_now/<int:id>', views.Buy_now, name='buy_now'),
    path('order_payment', views.Order_payment, name='order_payment'),
]
