from .models import Wishlist

def wishlist_count(request):
    count = Wishlist.objects.count()

    return {
        'wishlist_count': count
    }