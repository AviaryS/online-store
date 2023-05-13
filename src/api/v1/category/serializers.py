from rest_framework import serializers

from apps.product.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategories')

    def get_subcategories(self, obj):
        subcategories = CategorySerializer(obj.subcategories.all(), many=True).data
        return subcategories