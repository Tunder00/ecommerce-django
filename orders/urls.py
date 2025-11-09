from django.urls import path
from . import views, admin_views

urlpatterns = [
    # Customer routes
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),

    # Admin routes
    path('admin/dashboard/', admin_views.admin_dashboard, name='admin_dashboard'),
    path('admin/manage_orders/', admin_views.manage_orders, name='manage_orders'),
    path('admin/export_csv/', admin_views.export_orders_csv, name='export_orders_csv'),
]
