from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from User.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(unique=True)
    product_price = models.FloatField(default=0.0)
    product_quantity = models.IntegerField(default=0)
    product_short_description = models.TextField(blank=True, db_index=True, max_length=30)
    product_description = models.TextField(blank=True, db_index=True)
    product_is_published = models.BooleanField(default=False)
    product_type = models.CharField(max_length=30, db_index=True)
    product_seller = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='seller')

    def get_absolute_url(self):
        return reverse('shop', args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)


class ProductPhoto(models.Model):
    product_photo = models.ImageField(upload_to='product_photos/%Y/%m/%d', )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photo')

# class ProductSpecs(models.Model):
