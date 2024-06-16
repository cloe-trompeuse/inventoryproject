from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Order_1

@receiver(post_save, sender=Order_1)
def update_product_qty_on_save(sender, instance, **kwargs):
    product = instance.product
    product.quantity -= instance.orderQty
    product.save()

# @receiver(post_delete, sender=Order_1)
# def update_product_qty_on_delete(sender, instance, **kwargs):
#     product = instance.product
#     product.quantity += instance.orderQty
#     product.save()