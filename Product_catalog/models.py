from django.db import models
from django.contrib.auth.models import User

class Product_category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural ='Product_category'

    def __str__(self) -> str:
        return f"{self.name}"    
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Product_category, on_delete=models.CASCADE, related_name='categories')
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return f"{self.name} || {self.category}"