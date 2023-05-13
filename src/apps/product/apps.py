from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.product'

    verbose_name = 'Взаимодействие с продуктами'

    def ready(self):
        from apps.product.signals import update_cart_price
