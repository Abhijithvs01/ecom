
from .models import Order

def cart_count(request):
    try:
        count = 0
        if request.user.is_authenticated:
        
            customer = request.user.Customer_Profile

            cart = Order.objects.filter(
                owner=customer,
                order_status=Order.CART_STAGE
                ).first()

            if cart:
                count = cart.added_items.count()
            print(count)
            
        return { 'cart_count' : count }
    except Exception as e:
        print(e)
        return { 'cart_count' : count }
