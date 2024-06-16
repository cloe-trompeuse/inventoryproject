from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product, Order_1, Customer
from .forms import ProductForm, OrderForm, OrderUpdateForm, CustomerForm
from django.contrib import messages

"""
handle POST requests for creating new orders:
- Validate OrderForm
- Save order if valid and update product quantity
- Redirect to 'index' upon successful order creation

handle GET requests to display existing orders and order form:
- Retrieves all orders
- Initialize an empty OrderForm instance
"""
@login_required(login_url='user-login')
def index(request): 
    orders = Order_1.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.orderedBy = request.user
            product = instance.product
            if product.quantity >= instance.orderQty:
                instance.save()
                product.quantity -= instance.orderQty
                product.save()
                return redirect('index')
            else:
                messages.error(request, 'Quantity ordered exceeds available stock')
                pass
    else:
        form = OrderForm()

    context = {
        'orders': orders,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)

"""
retrieve all users
"""
@login_required(login_url='user-login')
def user(request):
    users = User.objects.all()

    users_count = users.count()

    context = {
        'users': users,
    }

    return render(request, 'dashboard/user.html', context)

"""
retrieve specific user by primary key
"""
@login_required(login_url='user-login')
def user_detail(request, pk):
    users = User.objects.get(id=pk)

    context = {
        'users': users,
    }

    return render(request, 'dashboard/user_detail.html', context)


"""
retrieve a specific user by primary key
handle POST requests for user deletion
"""
@login_required(login_url='user-login')
def user_delete(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('user')
    
    return render(request, 'dashboard/user_delete.html')

"""
retrieve all products
handle POST requests for adding new products
"""
@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('prodName')
            messages.success(request, f'{product_name} successfully added')

            return redirect('product')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form': form,
    }

    return render(request, 'dashboard/product.html', context)

"""
Retrieve a specific product by primary key
handle POST requests for product deletion
"""
@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('product')
    
    return render(request, 'dashboard/product_delete.html')

"""
retrieve a specific product by primary key
handle POST requests for updating product details
"""
@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(instance=item)

    context = {
        'form': form,
    }

    return render(request, 'dashboard/product_update.html', context)

"""
retrieve all orders
"""
@login_required(login_url='user-login')
def order(request):
    orders = Order_1.objects.all()

    context = {
        'orders': orders,
    }

    return render(request, 'dashboard/order.html', context)

"""
retrieve a specific order by primary key
handle POST requests for updating order details
"""
@login_required(login_url='user-login')
def order_update(request, pk):
    order = Order_1.objects.get(id=pk)
    
    if request.method == 'POST':
        order_form = OrderUpdateForm(request.POST, instance=order)
        if order_form.is_valid():
            order_form.save()
            return redirect('order')
    else:
        order_form = OrderUpdateForm(instance=order)

    context = {
        'order_form': order_form, 
    }

    return render(request, 'dashboard/order_update.html', context)

"""
retrieve a specific order by primary key
handle POST requests for order deletion and adjust product quantity
"""
@login_required(login_url='user-login')
def order_delete(request, pk):
    order = Order_1.objects.get(id=pk)

    if request.method == 'POST':
        product = order.product
        product.quantity += order.orderQty
        product.save()
        order.delete()
        return redirect('order')
    
    return render(request, 'dashboard/order_delete.html')

"""
retrieve all existing customers
"""
@login_required(login_url='user-login')
def customer(request):
    customers = Customer.objects.all()

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
            customer_form.save()
            customer_name = customer_form.cleaned_data.get('customer_name')
            messages.success(request, f'{customer_name} successfully added')

            return redirect('customer')
    else:
        customer_form = CustomerForm()

    context = {
        'customers': customers,
        'customer_form': customer_form,
    }

    return render(request, 'dashboard/customer.html', context)

"""
retrieve a specific customer by primary key
handle POST requests for updating customer details
"""
@login_required(login_url='user-login')
def customer_update(request, pk):
    customer = Customer.objects.get(id=pk)
    
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('customer')
    else:
        customer_form = CustomerForm(instance=customer)

    context = {
        'customer_form': customer_form, 
    }

    return render(request, 'dashboard/customer_update.html', context)

"""
retrieve a specific customer by primary key
handle POST requests for customer deletion and adjust product quantity
"""
@login_required(login_url='user-login')
def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer')
    
    return render(request, 'dashboard/customer_delete.html')