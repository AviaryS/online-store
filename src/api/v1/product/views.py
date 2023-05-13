from rest_framework import status
from rest_framework.decorators import api_view

from api.v1.product.utils import (
    filter_products_by_conditions, get_filter_params, serialize_products, serialize_product, get_product_by_id
)

from utils.response import make_response


@api_view(["GET"])
def product_list_view(request):
    """Возращает отфильтрованный по трем параметрам массив продуктов"""
    category_id, min_price, max_price = get_filter_params(request)

    products = filter_products_by_conditions(category_id, min_price, max_price)

    data = serialize_products(products)
    return make_response(data, status.HTTP_200_OK)


@api_view(["GET"])
def product_detail_view(request, product_id):
    """Возращает все данные о продукте"""
    product = get_product_by_id(product_id)
    if not product:
        return make_response({'error': f'Product with id {product_id} does not exist'}, status.HTTP_404_NOT_FOUND)
    data = serialize_product(product)
    return make_response(data, status.HTTP_200_OK)
