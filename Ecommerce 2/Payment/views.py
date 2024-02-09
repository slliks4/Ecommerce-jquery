from django.shortcuts import render,redirect
from Cart .models import *
from Payment .models import *
from Order_management .models import *

def Check_out(request):
    if request.user.is_authenticated:
        order_items = Order_items.objects.filter(customer = request.user, selected = True)
        checkout = Checkout.objects.create(customer=request.user,complete=True)
        checkout.order_items.set(order_items)
        for order_item in order_items:
            order_history = Order_history.objects.create(
                customer=request.user,
                product=order_item.product,
                quantity=order_item.quantity,
                price=12.3,
            )
            order_history.save()
        
        order_items.delete()
        checkout.delete()
        return render(request, 'checkout.html')
    else:
        return redirect('home')