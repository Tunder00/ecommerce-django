from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def home(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
