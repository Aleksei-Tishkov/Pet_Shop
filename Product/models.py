from django.db import models


class Product(models.Model):
    product_name = models.CharField(default='Default_Product_Name', max_length=30, db_index=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0.0)
    description = models.TextField(blank=True, db_index=True)
    is_published = models.BooleanField(default=False)


class ProductSpecs(models.Model):
    product_photos = []

    def add_photo(self, photo):
        self.product_photos.append(photo)