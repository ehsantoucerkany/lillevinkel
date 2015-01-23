from rest_framework import serializers

from .models import Product
from webshop.models import ProductVariant, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'id',
            'name'
        ]


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

    def get_image(self, product_variant):
        return self.context['request'].build_absolute_uri(product_variant.image)


class ProductListSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'brand',
            'description',
            'variants'
        ]
