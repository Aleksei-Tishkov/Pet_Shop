from django.contrib import admin
from Blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'time_create', 'is_published')
    list_editable = ('slug', 'is_published')
