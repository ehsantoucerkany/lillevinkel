from webshop.models import Product
from rest_framework import viewsets
from .serializers import ProductListSerializer
from rest_framework.response import Response


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
