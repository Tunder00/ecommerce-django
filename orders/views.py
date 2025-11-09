from django.shortcuts import render, redirect
from products.models import Product
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def cart_view(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')  
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total = sum(p.price for p in products)
    return render(request, 'orders/cart.html', {'products': products, 'total': total})

@login_required
def checkout(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total = sum(p.price for p in products)
    order = Order.objects.create(user=request.user, total=total)
    for p in products:
        OrderItem.objects.create(order=order, product=p, quantity=1)
    request.session['cart'] = []
    return render(request, 'order_success.html', {'order': order})

@login_required
def my_orders(request):
    """Display all orders for the logged-in user"""
    if request.user.is_staff:
        return redirect('admin_dashboard')
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})



from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def order_detail(request, order_id):
    """Display detailed view of a single order"""
    if request.user.is_staff:
        return redirect('admin_dashboard')
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = OrderItem.objects.filter(order=order)
    return render(request, 'orders/order_detail.html', {
        'order': order,
        'items': items
    })

