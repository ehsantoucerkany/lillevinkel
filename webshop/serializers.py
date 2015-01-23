from rest_framework import serializers

from .models import Product
from webshop.models import ProductVariant


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            'id',
            'color',
            'price',
            'size',
            'image',
            'quantity'
        ]


class ProductListSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'variants'
        ]
