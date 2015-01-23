from webshop.models import Product
from rest_framework import viewsets
from .serializers import ProductListSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
