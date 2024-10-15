from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.forms import LoginForm, RegistrationForm
from django.urls import path
from core.models import User, Product, Cart, Order

def real_index(request):
    return redirect('index')

def index(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('products')

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request, username=login_form.cleaned_data['email'], password=login_form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.success(request, "You are now logged in")
                return redirect('index')
            else:
                messages.error(request, "Username or password is incorrect")
    else:
        login_form = LoginForm()
    

    print("here")

    
    return render(request, 'login.html', {'login_form': login_form})

def register(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            new_user = User.objects.create_user(
                email=registration_form.cleaned_data['email'],
                password=registration_form.cleaned_data['password']
            )
            login(request, new_user)
            messages.success(request, "You were successfully registered")
            return redirect('index')
        else:
            messages.error(request, registration_form.errors)
    else:
        registration_form = RegistrationForm()

    login_form = LoginForm()
    return render(request, 'register.html', {'action': 'register', 'login_form': login_form, 'registration_form': registration_form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('index')

@login_required
def user_profile(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        physical_address = request.POST['physical_address']

        user.name = name
        if "@" in email:
            user.email = email
        else:
            messages.error(request, 'Email must have @')
            return redirect('user_profile')
        if len(password) < 4:
            messages.error(request, "Password must be of length greater than 4")
            return redirect('user_profile')
        if not any(c in special_characters for c in password):
            messages.error(request, 'Password must have at least one special character')
            return redirect('user_profile')

        user.set_password(password)
        user.physical_address = physical_address
        user.save()
        messages.success(request, 'Successfully updated')
        return redirect('user_profile')

    return render(request, 'user_profile.html')
 
def product(request, id): 
    product = get_object_or_404(Product, id=id)
    author = product.author_name

    has_ordered = Order.objects.filter(product_id=id, user_id=request.user.id).exists()

    return render(request, 'product.html', {'product': product, 'author': author})

@login_required
def add_to_cart(request, product_id):
    Cart.objects.create(user_id=request.user.id, product_id=product_id, quantity=1)
    messages.success(request, 'Product added to cart')
    return redirect('index')

@login_required
def checkout(request):
    if request.method == 'POST':
        orders = Cart.objects.filter(user_id=request.user.id)
        for order in orders:
            Order.objects.create(user_id=request.user.id, product_id=order.product_id)
            order.delete()
        messages.success(request, "Checkout successful")
        return redirect('index')

    user_cart = Cart.objects.filter(user_id=request.user.id)
    user_products = [item.product for item in user_cart]
    total_price = sum(item.product.price for item in user_cart)

    return render(request, 'checkout.html', {'total_price': total_price, 'products': user_products, 'cart_products': len(user_products)})

urlpatterns = [
    path('', real_index, name='real_index'),
    path('products/', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('user_profile/', user_profile, name='user_profile'),
    path('product/<int:id>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
]