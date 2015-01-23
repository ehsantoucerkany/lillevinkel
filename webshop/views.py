from rest_framework import viewsets
from rest_framework.response import Response

from webshop.models import Product, Brand
from .serializers import ProductListSerializer
from webshop.serializers import BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    model = Product

    def get_queryset(self):
        return Product.objects.all().prefetch_related('variants')

    def get_serializer_class(self):
        return ProductListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    model = Brand

    def get_queryset(self):
        return Brand.objects.all()

    def get_serializer_class(self):
        return BrandSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)
