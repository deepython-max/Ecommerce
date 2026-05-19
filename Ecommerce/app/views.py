from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    if not request.session.get('user_id'):
        return redirect('login')

    name = request.session.get('user_name')
    products = Product.objects.all()

    context = {
        'name': name,
        'products': products
    }

    return render(request, 'index.html', context)


# def index(request):
#     if request.user.is_anonymous:
#         return redirect('login')

#     name = request.user.username
#     return render(request, 'index.html', {'name': name})

def bestseller(request):
    return render(request, 'bestseller.html')

def cheackout(request):

    items = CartItem.objects.all()

    subtotal = 0

    for i in items:
        i.subtotal = i.product.price * i.quantity
        subtotal += i.subtotal

    total = subtotal

    context = {
        'items': items,
        'subtotal': subtotal,
        'total': total,
    }

    if request.method == "POST":
        Cheakout.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            conmpany_name=request.POST.get('conmpany_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            country=request.POST.get('country'),
            zip_code=request.POST.get('zip_code'),
            notes=request.POST.get('notes')
        )

        return redirect('thankyou')

    return render(request, 'cheackout.html', context)

# def contact(request):
#     return render(request, 'contact.html')

# def contact(request):
#     if request.method == "POST":

#         name = request.POST.get('name')

#         ContactMessage.objects.create(
#             name=name,
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             project=request.POST.get('project'),
#             subject=request.POST.get('subject'),
#             message=request.POST.get('message')
#         )

#         return redirect('thankyou')

#     return render(request, 'contact.html')

def contact(request):
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project = request.POST.get('project')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database 
        ContactMessage.objects.create( #this will save the data to the database
            name=name,
            email=email,
            phone=phone,
            project=project,
            subject=subject,
            message=message
        )

        # Send Thank You Mail to User
        send_mail(
            subject="Thank You For Contacting Us",
            message=f"""
            Hello {name},

            Thank you for contacting us.

            We have received your message regarding "{subject}" and will get back to you soon.

            Regards,
            Your Website Team
            """,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
                )

        return redirect('thankyou')

    return render(request, 'contact.html')

def thankyou(request):
    return render(request, 'thankyou.html', {'name': ContactMessage.objects.last().name})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def shop(request):

    query = request.GET.get('query')

    products = Product.objects.all()

    # search functionality
    if query:
        products = products.filter(name__icontains=query)

    # pagination
    paginator = Paginator(products, 4)

    page = request.GET.get('page')

    try:
        products = paginator.page(page)

    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    wishlist_item= Wishlist.objects.all()
    wishlist_count = wishlist_item.count()
    cart_items = CartItem.objects.all()
    cart_count = cart_items.count()

    context = {
        'products': products,
        'query': query,
        # 'wishlist_item': wishlist_item,
        'wishlist_count': wishlist_count,
        'cart_count': cart_count
    }

    return render(request, 'shop.html', context)

def single(request):
    return render(request, 'single.html')

def error_404(request):
    return render(request, '404.html')

def registration(request):
    if request.method == "POST":

        # ✅ 1. Get data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        # ✅ 2. ADD YOUR VALIDATION HERE 👇
        errors = []

        if Register.objects.filter(email=email).exists():
            errors.append("Email already exists ❌")

        if Register.objects.filter(name=name).exists():
            errors.append("Name already exists ❌")

        # ✅ 3. Check errors
        if errors:
            for error in errors:
                messages.error(request, error)

        else:
            # ✅ 4. Save only if no errors
            Register.objects.create(
                name=name,
                email=email,
                mobile=mobile,
                password=password
            )
            messages.success(request, f"Welcome {name}, registration successful ✅")  #this message will show on the redirected page if there is message tag inside that page's HTML and if not then it will show on the current page (registration.html page for this)
            return redirect('/login')

    # ✅ 5. Always return page
    return render(request, "register.html")

def loginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Register.objects.filter(email=email).first()

        if user:
            if user.password == password:
                request.session['user_id'] = user.id   # ✅ STORE SESSION
                request.session['user_name'] = user.name

                # request.session = {'user_id': 5,
                #                    'user_name': 'Deep'
                #                   }
                

                messages.success(request, "Login successful ✅")
                return redirect('home')
            else:
                messages.error(request, "Wrong password ❌")
        else:
            messages.error(request, "Email does not exist ❌")

    return render(request, "login.html")

def logoutUser(request):
    request.session.flush()   # 🔥 clears session  'request.session = {}'
    messages.success(request, "Logged out successfully ✅")
    return redirect('login')

# def registration(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         errors = []

#         if User.objects.filter(username=name).exists():
#             errors.append("Username already exists ❌")

#         if User.objects.filter(email=email).exists():
#             errors.append("Email already exists ❌")

#         if errors:
#             for error in errors:
#                 messages.error(request, error)
#         else:
#             # 🔥 create user (password automatically hashed)
#             user = User.objects.create_user(
#                 username=name,
#                 email=email,
#                 # password=password
#                 password=make_password(password)
#             )
            

#             messages.success(request, "Registration successful ✅")
#             return redirect('login')

#     return render(request, "register.html")

# def loginUser(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # 🔥 Django uses username by default
#         user = User.objects.filter(email=email).first()

#         if user:
#             user = authenticate(request, username=user.username, password=password)

#             if user is not None:
#                 login(request, user)   # ✅ session handled automatically
#                 print('hello')
#                 messages.success(request, "Login successful ✅")
#                 print('hello123')
#                 return redirect('home')
#             else:
#                 messages.error(request, "Wrong password ❌")
#         else:
#             messages.error(request, "Email does not exist ❌")

#     return render(request, "login.html")

# def logoutUser(request):
#     logout(request)   # ✅ built-in logout
#     messages.success(request, "Logged out successfully ✅")
#     return redirect('login')


# def logoutUser(request):
#     logout(request)   # ✅ built-in logout
#     messages.success(request, "Logged out successfully ✅")
#     return redirect('login')


def category(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)

    context = {
        'products': products,
        'category': category,
    }

    return render(request, 'shop.html', context)

def search_item(request):
    query = request.GET.get('query', '')   # matches HTML name

    products = Product.objects.all()  # start with all products

    if query:
        products = products.filter(name__icontains=query)

    return render(request, 'shop.html', {
        'products': products,
        'query': query
    })

def add_to_cart(request, id):
    if not request.session.get('user_id'):
        return redirect('login')

    user = Register.objects.get(id=request.session.get('user_id'))
    product = Product.objects.get(id=id)

    cart, created = Cart.objects.get_or_create(user=user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart')

def plus_cart(request, id):
    item = CartItem.objects.get(id=id)
    item.quantity += 1
    item.save()
    return redirect('cart')


def minus_cart(request, id):
    item = CartItem.objects.get(id=id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


def remove_cart(request, id):
    item = CartItem.objects.get(id=id)
    item.delete()
    return redirect('cart')

def cart(request):
    if not request.session.get('user_id'):
        return redirect('login')

    user = Register.objects.get(id=request.session.get('user_id'))

    cart, created = Cart.objects.get_or_create(user=user)

    items = CartItem.objects.filter(cart=cart)
    total = 0
    cart_items = CartItem.objects.all()
    cart_count = cart_items.count()

    for i in items:
        i.subtotal = i.product.price * i.quantity
        total += i.subtotal

    return render(request, 'cart.html', {
        'items': items,
        'total': total,
        'cart_count': cart_count
    })

from django.shortcuts import get_object_or_404, redirect

def add_wishlist(request, id):
    product = get_object_or_404(Product, id=id)

    existing = Wishlist.objects.filter(product=product)

    if existing.exists():
        existing.delete()
        return redirect('wishlist')
    else:
        Wishlist.objects.create(product=product)
        return redirect('shop')   # or redirect('shop')
    
# def remove_wishlist(request, id):
    
#     product = get_object_or_404(Product, id=id)
#     product.delete()
#     return redirect('wishlist') 

def remove_wishlist(request, id):
    wishlist_item = get_object_or_404(Wishlist, product_id=id)
    wishlist_item.delete()
    return redirect('wishlist')

def wishlist(request):
    wishlists = Wishlist.objects.all()
    wishlist_count = wishlists.count()

    return render(request, 'wishlist.html', {
        'wishlists': wishlists,
        'wishlist_count': wishlist_count
    })

