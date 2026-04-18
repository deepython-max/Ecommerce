from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Register
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    if not request.session.get('user_id'):
        return redirect('login')

    name = request.session.get('user_name')

    return render(request, 'index.html', {'name': name})

def bestseller(request):
    return render(request, 'bestseller.html')

def cart(request):
    return render(request, 'cart.html')

def cheackout(request):
    return render(request, 'cheackout.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

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
            messages.success(request, f"Welcome {name}, registration successful ✅")
            return redirect('/login')

    # ✅ 5. Always return page
    return render(request, "register.html")

def login(request):
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
