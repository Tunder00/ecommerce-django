from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order
import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def admin_dashboard(request):
    total_orders = Order.objects.count()
    total_revenue = sum(o.total for o in Order.objects.all())
    pending = Order.objects.filter(status='Pending').count()

    return render(request, 'orders/admin_dashboard.html', {
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'pending': pending,
    })


@login_required
def manage_orders(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        order = get_object_or_404(Order, id=order_id)
        order.status = new_status
        order.save()
        messages.success(request, f"Order #{order.id} status updated to {new_status}")
        return redirect('manage_orders')

    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/manage_orders.html', {'orders': orders})



@login_required
def export_orders_csv(request):
    if not request.user.is_staff:
        return redirect('home')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    writer = csv.writer(response)
    writer.writerow(['Order ID', 'User', 'Status', 'Total', 'Created'])
    for o in Order.objects.all():
        writer.writerow([o.id, o.user.username, o.status, o.total, o.created_at])
    return response
