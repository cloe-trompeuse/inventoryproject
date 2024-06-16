from django import forms
from .models import Product, Order_1, Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prodName', 'category', 'quantity']
        
class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order_1
        fields = ['product', 'orderQty', 'customer']

class OrderUpdateForm(forms.ModelForm):
    class Meta: 
        model = Order_1
        fields = ['product', 'orderQty', 'status', 'customer']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name', 'email', 'phone']