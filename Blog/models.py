from django.db import models
from django.urls import reverse
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField, SearchVector

from User.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Post.Status.PUBLISHED)


class Post(models.Model):
    class Meta:
        ordering = ['-time_create']
        indexes = [GinIndex(fields=["search_vector", ]), ]

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=75, unique=True, db_index=True, verbose_name='URL')
    main_photo = models.ImageField(upload_to='blog_photos/%Y/%m/%d',
                                   blank=True, verbose_name='Main photo')
    summary = models.TextField(max_length=256, db_index=True)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField('PostTag', blank=True, related_name='tags')

    search_vector = SearchVectorField(null=True)

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post', args=(self.slug, ))

    def __str__(self):
        return f'{self.title}'

    def update_search_vector(self):
        Post.objects.filter(pk=self.pk).update(search_vector=SearchVector('title', 'content', 'summary'))
        return


class PostTag(models.Model):
    tag_name = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='Tag')
    tag_slug = models.SlugField(max_length=20, unique=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.tag_slug})

    def __str__(self):
        return self.tag_name.title()
