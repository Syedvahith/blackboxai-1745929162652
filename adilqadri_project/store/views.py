
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Category
from django.views.decorators.http import require_POST

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Category
from django.views.decorators.http import require_POST

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.all()
    print("Number of products:", products.count())
    for product in products:
        print(f"Product: {product.name} - Price: {product.price}")
    return render(request, 'store/product_list.html', {'products': products})

def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/product_list.html', {'products': products, 'category': category})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})

@require_POST
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_detail', slug=slug)

@login_required
def cart_view(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart_items = []
        total_price = 0
    else:
        cart = Cart.objects.get(id=cart_id)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def update_cart_item(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = CartItem.objects.get(id=item_id)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return redirect('product_list')
    cart = Cart.objects.get(id=cart_id)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    if request.method == 'POST':
        # Placeholder for checkout processing (without payment)
        # Clear cart after checkout
        cart_items.delete()
        return render(request, 'store/checkout_success.html')
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def profile(request):
    return render(request, 'store/profile.html', {'user': request.user})
