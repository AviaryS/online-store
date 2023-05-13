from rest_framework import serializers

from apps.product.models.product import Product, ProductImage
from apps.product.models.review import Review


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ('id', 'image')

    def get_image(self, obj):
        host_name = 'http://localhost:8000/api/media/'
        image = host_name + str(obj.image) + '/'
        return image


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'text', 'rating', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'images', 'rating')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id')
        representation['rating'] = instance.get_rating()
        return representation


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)
    reviews_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description',
                  'price', 'extra_info', 'images',
                  'rating', 'reviews', 'reviews_count')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id')
        representation['rating'] = instance.get_rating()
        return representation

    def get_reviews_count(self, obj):
        return len(obj.reviews.all())