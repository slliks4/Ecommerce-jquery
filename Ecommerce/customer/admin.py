from django.contrib import admin
from .models import *

admin.site.register(Product_category)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Order_items)
admin.site.register(Shipping_address)
admin.site.register(Country)
admin.site.register(Payment)
admin.site.register(Order_history)
admin.site.register(Order_items_history)
