from django.shortcuts import render
from .models import *

def OrderHistory(request):
    try:
        order_histories = Order_history.objects.filter(customer = request.user)
    except:
        order_histories = []
    context = {
        'order_histories':order_histories
    }
    return render(request, 'order_history.html',context)