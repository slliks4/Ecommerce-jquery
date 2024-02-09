from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'customer')
    profile_pic = models.ImageField(upload_to='images', null= True , blank=True)
    tel = models.CharField(blank=True, max_length=16)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=400)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Customer(user=instance)
        user_profile.save()