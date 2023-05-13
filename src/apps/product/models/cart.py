from django.db import models

from apps.user.models import CustomUser


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='cart')
    price = models.DecimalField(verbose_name='Общая стоимость', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество продуктов', default=1)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'cart-id: {self.id}'

    @property
    def total_price(self):
        return sum(product.price for product in self.products.all())

    @property
    def total_quantity(self):
        return self.products.count()