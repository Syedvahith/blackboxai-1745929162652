from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cart/', views.cart_view, name='cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('profile/', views.profile, name='profile'),
    path('orders/', views.order_history, name='order_history'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
