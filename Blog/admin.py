from django.contrib import admin
from Blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'main_photo', 'summary', 'content', 'is_published')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', )
    list_display = ('title', 'slug', 'time_create', 'is_published')
    list_editable = ('slug', 'is_published')
    actions = ('publish_post', 'unpublish_post')

    @admin.action(description='Publish')
    def publish_post(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'Number of posts published: {count}.')

    @admin.action(description='Unpublish')
    def unpublish_post(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'Number of posts unpublished: {count}.', messages.WARNING)

