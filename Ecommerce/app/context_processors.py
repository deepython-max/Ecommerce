from .models import *

# def wishlist_count(request):
#     count = Wishlist.objects.count()

#     return {
#         'wishlist_count': count
#     }

def categories(request):
    return {
        'categories': Category.objects.all()
    }

