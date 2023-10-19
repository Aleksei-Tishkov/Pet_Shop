from django.db import models

# Create your models here.
import User_Accounts.models


class Post(models.Model):
    author = models.ForeignKey(User_Accounts.models.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=75, unique=True, db_index=True)
    main_photo = models.ImageField(blank=True)
    summary = models.TextField(max_length=255, blank=True, db_index=True)
    content = models.TextField(blank=True, db_index=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)