from django.db.models import Q

from api.v1.product.serializers import ProductSerializer, ProductDetailSerializer
from apps.product.models.product import Product


def get_product_by_id(product_id):
    try:
        return Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return None


def serialize_product(product):
    serializer = ProductDetailSerializer(product)
    return serializer.data


def serialize_products(products):
    serializer = ProductSerializer(products, many=True)
    return serializer.data


def get_filter_params(request):
    category_id = request.query_params.get("category_id")
    min_price = request.query_params.get("min_price")
    max_price = request.query_params.get("max_price")
    return category_id, min_price, max_price


def build_product_conditions(category_id=None, min_price=None, max_price=None):
    conditions = []
    if category_id:
        conditions.append(Q(category=category_id))
    if min_price and max_price:
        conditions.append(Q(price__gte=min_price) & Q(price__lte=max_price))
    elif min_price:
        conditions.append(Q(price__gte=min_price))
    elif max_price:
        conditions.append(Q(price__lte=max_price))
    return conditions


def filter_products_by_conditions(category_id=None, min_price=None, max_price=None):
    conditions = build_product_conditions(category_id, min_price, max_price)
    products = Product.objects.filter(*conditions)
    return products