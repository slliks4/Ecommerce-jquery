from django.db import models
from django.contrib.auth.models import User
from Order_management .models import Order_items


class Checkout(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    order_items = models.ManyToManyField(Order_items,related_name='all_order_items')
    complete = models.BooleanField(default=False)
