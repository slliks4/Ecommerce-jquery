from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User_profile.urls')),
    path('', include('Product_catalog.urls')),
    path('', include('Cart.urls')),
    path('', include('Payment.urls')),
    path('',include('Order_management.urls')),
]
