from rest_framework import serializers
from .models import Supplier, Category, Review, Product


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:

        model = Supplier
        fields = (
            'id',
            'name',
            'created',
            )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = (
            'id',
            'name',
            )


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:

        extra_kwargs = {
            'email':{'write_only': True}
        }

        model = Review
        fields = (
            'id',
            'product',
            'user_name',
            'email',
            'review',
            'rating',
            'created',
            'updated'
            )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = (
            'id',
            'name',
            'SKU',
            'supplier',
            'category',
            'price',
            'description',
            'created',
            'updated'
            )