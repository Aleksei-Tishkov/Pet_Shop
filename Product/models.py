from django.db import models

# Create your models here.
class Product(models.Model):
    def create_product(self, product_name, price, quantity, description, specs, photos=None, is_published=False):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.specs = specs
        self.photos = photos
        self.is_published = is_published