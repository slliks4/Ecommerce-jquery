from django.shortcuts import render,redirect,HttpResponsePermanentRedirect
from .models import *
from django.http import JsonResponse

def Customer_cart(request):
    if request.user.is_authenticated:
        order_items = Order_items.objects.filter(customer = request.user)
        get_total_price = 0

        for order_item in order_items:
            get_total_price += order_item.get_total

        context = {
            'order_items': order_items,
            'get_total_price':get_total_price,
        }
        return render(request, 'cart.html',context)
    else:
        order_items = []
        selected_items_count = ""
        context = {
            'order_items': order_items,
            'selected_items_count':selected_items_count,
        }
        return render(request, 'cart.html',context)

def Add_to_cart(request):
    if (request.user.is_authenticated):
        if (request.method == 'POST'):
            product_id = int(request.POST.get('product_id'))
            product = Products.objects.get(id=product_id)
            data = {
                'message': f'{product.name} added successfully'
            }
            if(product):
                order_item_exist = Order_items.objects.filter(customer=request.user, product=product)
                if (order_item_exist):
                    return JsonResponse({'message' : f'{product.name} already in cart'},status=400)
                else:
                    order_item = Order_items.objects.create(customer=request.user, product=product)
                    order_item.save()
                    return JsonResponse(data,status=200)
            else:
                return JsonResponse({'message' : 'no product with such id'},status=400)
        
        else:
            return redirect('home')
    else:
        return JsonResponse({'message' : 'you must be logged in to perfom this operation'},status=400)

def Edit_cart_items(request):
    if request.method == 'POST':
        if (request.user.is_authenticated):   
            order_item_id = int(request.POST.get('order_item_id'))
            order_items = Order_items.objects.get(id=order_item_id)
            data = {
                'message': f'{order_items.product.name} quantity changed successfully'
            }
            if (order_items):
                quantity_val = int(request.POST.get('quantity_val'))
                order_items.quantity = quantity_val
                order_items.save()
                return JsonResponse(data)
            else:
                return JsonResponse({'message': 'order_item does not exist'})
        else:
            return redirect('home')
    else:
        return redirect('cart')
    
def Delete_order_item(request):
    if (request.user.is_authenticated):
        if (request.method == 'POST'):
            id = int(request.POST.get('order_item_id'))
            order_item = Order_items.objects.get(id=id, customer=request.user)
            data = {
                'message': f'{order_item.product.name} deleted successfully'
            }
            if (order_item):
                order_item.delete()
                return JsonResponse(data)
            else:
                return JsonResponse({'message': 'order_item does not exist'})
        else:
            return redirect('cart')
    else:
        return redirect('home')
    
def Order_item_select(request):
    if (request.user.is_authenticated):
        if (request.method == 'POST'):
            id = int(request.POST.get('order_item_id'))
            selected = request.POST.get('selected')
            order_item = Order_items.objects.get(id=id, customer=request.user)
            if (order_item):
                if selected == 'select':
                    order_item.selected = True
                    order_item.save()
                    return JsonResponse({'message': 'selected'})
                elif selected == 'unselect':
                    order_item.selected = False
                    order_item.save()
                    return JsonResponse({'message': 'unselected'})
            else:
                return JsonResponse({'message': 'order_item does not exist'})
        else:
            return redirect ('cart')
    else:
        return redirect('home')
    
from django.http import JsonResponse

def Select_all(request):
    order_items = Order_items.objects.filter(customer=request.user)
    if request.method == 'POST':
        select_all = request.POST.get('select_all')

        if select_all == 'select':
            for order_item in order_items:
                order_item.selected = True
                order_item.save()

        elif select_all == 'unselect':
            for order_item in order_items:
                order_item.selected = False
                order_item.save()

    return redirect('cart')
