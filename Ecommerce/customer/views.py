from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .models import *
from .forms import *
from django.http import Http404,JsonResponse
from django.urls import reverse_lazy
from django.http import HttpResponseServerError

def Home(request):
    products = Products.objects.all()
    try:
        order= Order.objects.get(customer=request.user.customer_profile)
    except:
        order = []
    context = {
        'products':products,
        'order':order
    }
    return render(request, 'index.html',context)

def Product_view(request,id,name,category):
    if request.user.is_authenticated:
        product = Products.objects.get(id=id)
        try:
            order = Order.objects.get(customer=request.user.customer_profile)
        except:
            order = []
        is_order_complete = product.products.filter(order=order)
        context = {
            'product': product,
            'order':order,
            'is_order_complete': is_order_complete,
        }
        return render(request, 'product_view.html',context)
    else:
        return redirect('home')

def Search_product(request):
    pass

def Orders_history(request):
    if request.user.is_authenticated:
        customer = request.user.customer_profile
        orders = Order_history.objects.filter(customer=request.user.customer_profile)
        order_items = []
        order = Order.objects.get(customer=customer)
        context = {
            'order':order,
            'order_items':order_items
        }
        for order in orders:
            order_items.extend(order.order_items_history.all())
        return render(request,'order_history.html', context)
    else:
        return redirect('home')

def Add_to_cart(request,id):
    product = Products.objects.get(id=id)
    customer = request.user.customer_profile
    order, created = Order.objects.get_or_create(customer=customer)
    order_item, created = Order_items.objects.get_or_create(products=product,order=order)
    return redirect('home')

def Customer_cart(request):
    if request.user.is_authenticated:
        order_tuple = Order.objects.get_or_create(customer=request.user.customer_profile)
        order = order_tuple[0]
        order_items = order.order_item.all()
        context = {
            'order_items': order_items,
            'order':order
        }
        return render(request, 'cart.html', context)
    
    else:
        return redirect('home')
    
def Order_item_delete(request,id):
    order_item = Order_items.objects.get(id=id)
    order_item.delete()
    return redirect('customer_cart')

def Edit_order_items(request,id):
    order_item = get_object_or_404(Order_items, id=id)
    if request.method == 'POST':
        change_quantity = request.POST.get('change_quantity')
        selected = request.POST.get('selected')
        try:
            if change_quantity == 'remove_cart':
                order_item.quantity -= 1
                order_item.save()
                if order_item.quantity == 0:
                    order_item.delete()
                return redirect('customer_cart')
            elif change_quantity == 'add_cart' :
                order_item.quantity += 1
                order_item.save()
                return redirect('customer_cart')
            if selected == 'select':
                order_item.selected = True
            elif selected == 'unselect':
                order_item.selected = False

            order_item.save()
            return redirect('customer_cart')

        except Exception as e:
            return HttpResponseServerError(f"An error occurred: {str(e)}")

def Select_all(request, id):
    order = Order.objects.get(customer=request.user.customer_profile, id=id)
    order_items = order.order_item.all()
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

    return redirect('customer_cart')

def Order_checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer_profile
        order = Order.objects.get(customer=customer)
        order_items = order.order_item.filter(selected=True)
        if request.method == 'POST':
            form = Add_shipping_address(request.POST)
            if form.is_valid():
                shipping_address = form.save(commit=False)
                shipping_address.order = order
                shipping_address.save()
                return HttpResponseRedirect(reverse_lazy('order_payment'))
            else:
                raise Http404('invalid details')
    else:
        return redirect('home')
    form = Add_shipping_address(instance=customer)
    context = {
        'order_items':order_items,
        'form':form,
        'order':order
        }
    return render(request, 'checkout.html',context)

def Buy_now(request,id):
    if request.user.is_authenticated:
        product = Products.objects.get(id=id)
    else:
        return redirect('home')
    return render(request, 'buy_now.html',{'product':product})    

def Order_payment(request):
    customer = request.user.customer_profile
    order = Order.objects.get(customer=customer)
    order_items = order.order_item.filter(selected=True)
    shipping = Shipping_address.objects.get(order=order)
    if request.method == 'POST':
        form = Complete_payment(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.save()
            order_history = Order_history.objects.create(
                customer=customer,
                total_price=order.get_total_price,
                total_order_items = order.get_cart_items,
                order_id=order.order_id
            )
            order_history.save()
            shipping.order_history = order_history
            shipping.save()
            new_shipping_address = Shipping_address.objects.get(order_history=order_history)
            for order_item in order_items:
                try:
                    order_items_history = Order_items_history.objects.create(
                        product=order_item.products,
                        order=order_history,
                        quantity=order_item.quantity,
                        price=order_item.get_total,
                    )
                    order_items_history.save()
                    order_items.delete()   
                except Exception as e:
                    # Handle the exception here (e.g., log the error, display a message)
                    print(f"Error creating order_items_history: {str(e)}")
            payment.delete()
            new_order = Order.objects.create(customer = customer)
            order_items_false = order.order_item.filter(selected = False)
            for order_item_false in order_items_false:
                order_item_false.order = new_order
                order_item_false.save()
            order.delete()
            return render(request, 'order_complete.html',{'order_history':order_history,'order_item':order_items_history,'shipping':new_shipping_address,})
        else:
            raise Http404('invalid')
 
    form = Complete_payment(instance=order)
    context = {
        'form':form, 
        'order_items':order_items,
        'order':order
        }
    return render(request, 'payment.html',context)
