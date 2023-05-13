from django.db import models

from apps.product.models.cart import Cart
from apps.product.models.category import Category


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=255)
    description = models.TextField(verbose_name='Описание товара', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    extra_info = models.JSONField(verbose_name='Дополнительная информация', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина', related_name='products',
                             blank=True, null=True)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'id: {self.id} - name: {self.name} - {self.cart}'

    def get_rating(self):
        """Returns the overall rating of the product based on its reviews"""
        reviews = self.reviews.all()
        if not reviews:
            return None

        total_rating = sum(review.rating for review in reviews)
        avg_rating = total_rating / len(reviews)
        return round(avg_rating, 1)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='images')
    image = models.ImageField(verbose_name='Фото продукта', upload_to='product_images/')

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фотки продукта'

    def __str__(self):
        return f'{self.product.name} - {self.image.name}'