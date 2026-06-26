from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Order, Order_item
from products.models import products  # FIXED IMPORT
from django.contrib import messages


# ---------------- CART VIEW ----------------
def cart(request):
    try:

        # If user not logged in → show page
        if not request.user.is_authenticated:
            return render(request, 'ifnouser.html')

        customer = request.user.Customer_Profile

        cart = Order.objects.filter(
            owner=customer,
            order_status=Order.CART_STAGE
            ).first()

        if cart:
            count = cart.added_items.count()
        else:
            count = 0

        print(count)
        
        return render(request, 'cart.html', {
            'cart': cart,
            'count':count
        })
    except Exception as e:
            print(e)  # Only visible in the terminal
            return render(request, "cart.html") 
    
@login_required(login_url='account')
def order(request):
    try:

        customer = request.user.Customer_Profile

        all_orders = Order.objects.filter(
            owner=customer
        ).exclude(order_status=Order.CART_STAGE)

        context = {
            'orders': all_orders
        }
        return render(request, "order.html", context)
    except Exception as e:
        print(e)
        return render(request, "order.html")

def checkout(request):
    if request.POST:
        user = request.user
        customer = request.user.Customer_Profile
        total = request.POST.get('total')
        Order_obj = Order.objects.get(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        if Order_obj:
            Order_obj.order_status = Order.ORDER_CONFIRMED
            Order_obj.save()
            return render(request, "sucess.html")
        else:
            return render(request,"failed.html")


def increase_quntity(request,id):
    item = get_object_or_404(Order_item, id = id)
    item.quantity += 1
    item.save()
    return redirect('cart')
def decrease_quntity(request,id):
    item = get_object_or_404(Order_item, id = id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    return redirect('cart')
def remove_from_cart(request,id):
    item = Order_item.objects.get(id = id)
    if item:
        item.delete()
    return redirect('cart')   
 
@login_required(login_url='account')   # or 'login'
def add_to_cart(request):
    try:

        if request.method == "POST":

            customer = request.user.Customer_Profile

            quantity = int(request.POST.get('quantity', 1))
            product_id = request.POST.get('product_id')
            size = request.POST.get('size')

            # get or create cart
            cart_obj, created = Order.objects.get_or_create(
                owner=customer,
                order_status=Order.CART_STAGE
            )

            # get product
            product = products.objects.get(pk=product_id)

            # get or create cart item
            ordered_item, created = Order_item.objects.get_or_create(
                product=product,
                owner=cart_obj,
                size=size
            )

            # update quantity correctly
            if created:
                ordered_item.quantity = quantity
            else:
                ordered_item.quantity += quantity

            ordered_item.save()
        return redirect('cart')
    except Exception as e:
        print(e)
        return redirect('cart')