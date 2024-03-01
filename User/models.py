from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from Pet_Shop import settings
from User.services import create_theme_entry_for_user


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='avatars/%Y/%m/%d', blank=True,
                                      default=settings.DEFAULT_USER_IMAGE,
                                      verbose_name='Avatar')
    user_slug = models.SlugField(unique=True)
    user_postalcode = models.PositiveIntegerField(blank=True)
    user_address = models.CharField(max_length=512, blank=True)

    def save(self, *args, **kwargs):
        self.user_slug = slugify(self.username)
        super().save(*args, **kwargs)


class UserTheme(models.Model):
    user_theme_user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='theme')
    user_theme_theme = models.IntegerField(default=0)

