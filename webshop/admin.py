from django.contrib import admin
from .models import Product, ProductVariant, Brand

admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Brand)
