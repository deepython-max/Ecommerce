from .models import Category, Cart, CartItem, Wishlist, Register

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def cart_context(request):
    cart_count = 0
    wishlist_count = Wishlist.objects.count()
    user_id = request.session.get('user_id')
    
    if user_id:
        user = Register.objects.filter(id=user_id).first()
        if user:
            cart = Cart.objects.filter(user=user).first()
            if cart:
                cart_items = CartItem.objects.filter(cart=cart)
                cart_count = sum(item.quantity for item in cart_items)
    else:
        cart_items = CartItem.objects.all()
        cart_count = sum(item.quantity for item in cart_items) if cart_items.exists() else 0
        
    return {
        'cart_count': cart_count,
        'wishlist_count': wishlist_count,
    }

