from django.db import models

# Create your models here.
#import User_Accounts.models
from django.urls import reverse

from User.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=75, unique=True, db_index=True, verbose_name='URL')
    main_photo = models.ImageField(upload_to='blog_photos/%Y/%m/%d',
                                   blank=True, verbose_name='Main photo')
    summary = models.TextField(max_length=255, db_index=True)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField('PostTag', blank=True, related_name='tags')

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post', args=(self.slug, ))

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


class PostTag(models.Model):
    tag_name = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='Tag')
    tag_slug = models.SlugField(max_length=20, unique=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.tag_slug})

    def __str__(self):
        return self.tag_name.title()