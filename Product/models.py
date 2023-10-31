from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(default='Default_Product_Name', max_length=30, db_index=True)
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True, db_index=True)
    is_published = models.BooleanField(default=False)
    product_type = models.CharField(default='Dog product', max_length=30, db_index=True)

    def get_absolute_url(self):
        return reverse('shop', args=(self.slug, ))

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.product_name)
    #     super().save(*args, **kwargs)


class ProductSpecs(models.Model):
    product_photos = []

    def add_photo(self, photo):
        self.product_photos.append(photo)