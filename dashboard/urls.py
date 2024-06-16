from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('user/delete/<int:pk>/', views.user_delete, name='user-delete'),
    path('user/detail/<int:pk>', views.user_detail, name='user-detail'),
    path('order/', views.order, name='order'),
    path('order/update/<int:pk>/', views.order_update, name='order-update'),
    path('order/delete/<int:pk>/', views.order_delete, name='order-delete'),
    path('product/delete/<int:pk>/', views.product_delete, name='product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='product-update'),
    path('product/', views.product, name='product'),
    path('customer/', views.customer, name='customer'),
    path('customer/delete/<int:pk>/', views.customer_delete, name='customer-delete'),
    path('customer/update/<int:pk>/', views.customer_update, name='customer-update'),
]

