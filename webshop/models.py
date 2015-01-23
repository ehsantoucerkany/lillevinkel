from django.db import models
from django.utils.encoding import smart_unicode


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return smart_unicode("Brand: " + self.name)


class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=False, null=False)
    brand = models.ForeignKey(to=Brand, blank=False, null=False)

    def __unicode__(self):
        return smart_unicode("Product: " + self.name)


class ProductVariant(models.Model):
    product = models.ForeignKey(to=Product, blank=False, null=False)

    price = models.FloatField(blank=False, null=False)
    size = models.FloatField(blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)

    image = models.ImageField()

    def __unicode__(self):
        return smart_unicode(
            "ProductVariant (product: " + self.product.name + ")"
            + " (size: " + str(self.size) + ")"
            + " (price: " + str(self.price) + ")"
        )
