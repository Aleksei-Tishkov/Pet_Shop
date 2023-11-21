from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from Pet_Shop import settings


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='avatars/%Y/%m/%d', blank=True,
                                      default=settings.DEFAULT_USER_IMAGE,
                                      verbose_name='Avatar')
    user_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.user_slug = slugify(self.username)
        super().save(*args, **kwargs)


