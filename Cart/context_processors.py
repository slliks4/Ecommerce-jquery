# context_processors.py

from .models import Order_items  # Import your Order_items model

def cart_count(request):
    if request.user.is_authenticated:
        order_items = Order_items.objects.filter(customer=request.user)
        return {'cart_count': order_items.count()}
    else:
        return {'cart_count': 0}
