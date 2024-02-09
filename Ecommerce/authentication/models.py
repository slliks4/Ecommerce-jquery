from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    tel = models.CharField(blank=True, max_length=16)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=400)
    payment_method_choice ={
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
    }
    payment_method = models.CharField(max_length=20, blank=True, choices=payment_method_choice, default='credit_card')
    profile_pic = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Customer_profile' 

    def __str__(self) -> str:
        return f"{self.user}"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Customer_profile(user=instance)
        user_profile.save()