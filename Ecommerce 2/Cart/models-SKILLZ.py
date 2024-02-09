from django.db import models
from django.contrib.auth.models import User
from Product_catalog .models import *

class Order_items(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name='order_items')
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    selected = models.BooleanField(default=False) 

    @property
    def get_total(self):
        price = self.quantity * self.product.price
        return price
    
    @property
    def get_selected_items_count(self):
        selected_items = Order_items.objects.filter(customer=self.customer, selected=True)
        total = selected_items.count()
        return total
    
    class Meta:
        verbose_name_plural = 'Order_items'
        ordering=('-date_added',)

    def __str__(self) -> str:
        return f"{self.customer} || {self.product} || {self.selected}"