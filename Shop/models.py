from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from Pet_Shop import settings
from User.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Product.Status.PUBLISHED)


class Product(models.Model):
    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'

    product_name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(unique=True)
    product_price = models.FloatField(default=0.0)
    product_main_photo = models.ImageField(upload_to='product_photos/%Y/%m/%d',
                                           default=settings.DEFAULT_PRODUCT_IMAGE)
    product_quantity = models.IntegerField(default=0)
    product_short_description = models.TextField(blank=True, db_index=True, max_length=30)
    product_description = models.TextField(blank=True, db_index=True)
    product_is_published = models.BooleanField(default=False)
    product_type = models.CharField(max_length=30, db_index=True)
    product_seller = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='seller')
    time_create = models.TimeField(auto_now_add=True)

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('shop', args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)


class ProductPhoto(models.Model):
    product_photo = models.ImageField(upload_to='product_photos/%Y/%m/%d', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photo')

# class ProductSpecs(models.Model):
