from django.urls import path
from .import views

urlpatterns = [
    path('checkout/',views.Check_out, name='checkout'),
]