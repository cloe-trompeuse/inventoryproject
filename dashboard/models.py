from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('Stationery', 'Stationery'),
    ('Hygiene', 'Hygiene'),
    ('Electronics', 'Electronics')
)

STATUS = (
    ('Pending', 'Pending'), 
    ('Completed', 'Completed')
)

#Product table
class Product(models.Model):
    prodName = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta: 
        verbose_name_plural = 'Product'

    #String representation of model data
    def __str__(self):
        return f'{self.prodName}-{self.category}-{self.quantity}'
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)

    class Meta: 
        verbose_name_plural = 'Customer'

    def __str__(self):
        return f'{self.customer_name}-{self.phone}-{self.email}'

class Order_1(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    orderedBy = models.ForeignKey(User, models.CASCADE, null=True)
    orderQty = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS, null=True)
    customer = models.ForeignKey(Customer, models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product}-{self.orderedBy}-{self.orderQty}-{self.date}-{self.status}-{self.customer}'