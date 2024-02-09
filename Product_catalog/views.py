from django.shortcuts import render,redirect
from .models import *
from Cart .models import *

def Home(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request, 'index.html',context)

def Product_view(request,id):
    product = Products.objects.get(id=id)
    context = {
        'product':product
    }
    return render(request, 'product_view.html', context)
