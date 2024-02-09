from django.db import models
from django.contrib.auth.models import User
from Product_catalog .models import *
from Cart .models import *
import uuid
from django.utils import timezone


class Order_history(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order_id = models.CharField(max_length=11, unique=True, editable=False)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    
    class Meta:
        verbose_name_plural = 'Order_history'
        ordering=('-date_added',)

    def __str__(self) -> str:
        return f"{self.customer} || {self.order_id}"
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            unique_id = str(uuid.uuid4().int)[:4]
            self.order_id = f"{timestamp}-{unique_id}-{self.customer.id}"
        super().save(*args, **kwargs)