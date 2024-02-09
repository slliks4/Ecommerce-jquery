from django.urls import path
from .import views

urlpatterns = [
    path('order_history/',views.OrderHistory, name='order_history'),
]