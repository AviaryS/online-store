from django.contrib import admin

from apps.product.models.cart import Cart
from apps.product.models.category import Category
from apps.product.models.product import Product, ProductImage
from apps.product.models.review import Review


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Cart)