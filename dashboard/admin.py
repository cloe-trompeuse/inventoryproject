from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group
from .models import Order_1, Customer

admin.site.site_header = 'DM IMS Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('prodName', 'category' ,'quantity',)
    list_filter = ['category']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'orderedBy', 'orderQty', 'date', 'status')
    list_filter = ['orderedBy']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone', 'email')
    list_filter = ['customer_name']

# Register created models(tables)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order_1, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
