from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import OrderForm, LoginForm
from .models import Product, CartItem, Category, Order


def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        session_key=request.session.session_key,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('/basket/')


def cart_view(request):
    cart_items = CartItem.objects.filter(session_key=request.session.session_key)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'basket.html', {'cart_items': cart_items, 'total': total})


def clear_cart(request):
    CartItem.objects.filter(session_key=request.session.session_key).delete()
    return redirect('/')


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'product': product})


def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'products': products, 'category': category, 'categories': categories})


def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            cart_items = CartItem.objects.filter(session_key=request.session.session_key)
            total = sum(item.total_price() for item in cart_items)
            data.price = total
            data.save()
            data.items.set(cart_items)
            data.save()
            return redirect('/')
    return render(request, 'create_order.html', {'form': form})


@login_required(login_url='/login/')
def panel(request):
    return render(request, 'ordersPanel.html', {'orders': Order.objects.all()})


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')


def redirect_home(req):
    return redirect('/')


class MyLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'


def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'order-details.html', {'order': order})
