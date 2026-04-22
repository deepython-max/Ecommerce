from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
    if not request.session.get('user_id'):
        return redirect('login')

    name = request.session.get('user_name')

    return render(request, 'index.html', {'name': name})


# def index(request):
#     if request.user.is_anonymous:
#         return redirect('login')

#     name = request.user.username
#     return render(request, 'index.html', {'name': name})

def bestseller(request):
    return render(request, 'bestseller.html')

def cart(request):
    return render(request, 'cart.html')

def cheackout(request):
    return render(request, 'cheackout.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    products = Product.objects.all()
    context = {'products': products}

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


    



