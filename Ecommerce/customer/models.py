from django.db import models
import requests 
from authentication .models import Customer_profile
import uuid
from django.utils import timezone

class Product_category(models.Model):
    category = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural ='Product_category'

    def __str__(self) -> str:
        return f"{self.category}"    
    

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
    
class Order(models.Model):
    customer = models.ForeignKey(Customer_profile,on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=11, unique=True, editable=False)
    
    @property
    def get_total_price(self):
        order_items = self.order_item.filter(selected = True )
        price = sum([item.get_total for item in order_items])
        return price
    
    @property
    def get_cart_items(self):
        order_items = self.order_item.all()
        total = len(order_items)
        return total
    
    @property
    def get_cart_items_selected(self):
        order_items = self.order_item.filter(selected = True)
        total = len(order_items)
        return total
    
    class Meta:
        verbose_name_plural ='Order'
        ordering=('-date_ordered',)

    def __str__(self) -> str:
        return f"{self.customer.user.username} || {self.order_id} "
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
            unique_id = str(uuid.uuid4().int)[:4]
            self.order_id = f"{timestamp}-{unique_id}-{self.customer.user.id}"
        super().save(*args, **kwargs)

class Order_items(models.Model):
    products = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True,related_name='products')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_item')
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    selected = models.BooleanField(default=False)

    @property
    def get_total(self):
        price = self.quantity * self.products.price
        return price
      
    class Meta:
        verbose_name_plural = 'Order_items'
        ordering=('-date_added',)

    def __str__(self) -> str:
        return f" {self.order} || {self.products}  || {self.selected}"

class Order_history(models.Model):
    customer = models.ForeignKey(Customer_profile,on_delete=models.CASCADE, editable=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    total_price = models.FloatField(null=True, blank=True, editable=False)
    total_order_items = models.IntegerField(editable=False,blank=True,null=True)
    order_id = models.CharField(max_length=100, null=True, blank=True, editable=False)

    class Meta:
        verbose_name_plural ='Order_history'
        ordering=('-date_ordered',)

    def __str__(self) -> str:
        return f"{self.customer.user.username} || {self.order_id} || total_order_items ( {self.total_order_items} )  || total-order-price: $ {self.total_price} ||  {self.complete}"


class Order_items_history(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, editable=False)
    order = models.ForeignKey(Order_history, on_delete=models.CASCADE, related_name='order_items_history', editable=False)
    quantity = models.IntegerField(editable=False)
    price = models.FloatField(null=True, blank=True, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order_items_history'
    
    def __str__(self) -> str:
        return f"{self.order.customer.user.username} || {self.order.order_id} || {self.product} ||  price : ${self.price} || {self.order.complete} "
    
class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    population = models.IntegerField()
    
    def fetch_country_data(cls, country_code):
        url = f"https://api.example.com/countries/{country_code}"  
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return cls(
                name=data['name'],
                capital=data['capital'],
                population=data['population']
            )
        else:
            return None
            
class Shipping_address(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True, blank=True,related_name='order')
    order_history = models.ForeignKey(Order_history, on_delete=models.CASCADE, null= True, blank=True)
    email = models.EmailField()
    email_news = models.BooleanField(default=True)
    DELIVERY_OPTIONS = [
        ('SHIP', 'ship'),
        ('PICKUP', 'pick up'),
    ]
    delivery_option = models.CharField(max_length=100, choices=DELIVERY_OPTIONS)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,blank=True,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    appartment = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Shipping_address'

    def __str__(self) -> str:
        return f"{self.email}"
    
class Payment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True, blank=True)
    BILLING_ADDRESS = [
        ('SHIPPING_ADDRESS','same as shipping address'),
        ('DIFFERENT','different billing address'),
    ]
    billing_address = models.CharField(choices=BILLING_ADDRESS,null=True,blank=True,max_length=200)
    remember_me = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Payment'

    def __str__(self) -> str:
        return f"{self.order}"