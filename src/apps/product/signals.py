from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.product.models.product import Product


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def update_cart_price(sender, instance, **kwargs):
    cart_id = instance.cart_id
    products = Product.objects.filter(cart_id=cart_id)
    cart = products.first().cart
    cart.price = cart.total_price
    cart.quantity = cart.total_quantity
    cart.save()