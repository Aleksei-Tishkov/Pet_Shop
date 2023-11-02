from django.db import models

# Create your models here.
#import User_Accounts.models
from django.urls import reverse


class Post(models.Model):
    #author = models.ForeignKey(User_Accounts.models.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=75, unique=True, db_index=True, verbose_name='URL')
    main_photo = models.ImageField(upload_to='blog_photos/%Y/%m/%d',
                                   blank=True, verbose_name='Main photo')
    summary = models.TextField(max_length=255, db_index=True)
    content = models.TextField(db_index=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('post', args=(self.slug, ))
