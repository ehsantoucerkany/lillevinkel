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

    def get_image(self, product_variant):
        return self.context['request'].build_absolute_uri(product_variant.image)

class ProductListSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'variants'
        ]
