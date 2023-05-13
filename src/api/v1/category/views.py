from rest_framework import status
from rest_framework.decorators import api_view

from api.v1.category.serializers import CategorySerializer
from apps.product.models.category import Category

from utils.response import make_response


@api_view(["GET"])
def category_list_view(request):
    """Возращает все основные категории и их подкатегории"""
    categories = Category.objects.filter(parent_category=None)
    serializer = CategorySerializer(categories, many=True)
    return make_response(serializer.data, status.HTTP_200_OK)