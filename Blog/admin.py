from django.contrib import admin
from django.utils.safestring import mark_safe

from Blog.models import Post, PostTag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'tags', 'main_photo', 'post_photo', 'summary', 'content', 'is_published')
    readonly_fields = ('post_photo', )
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', )
    filter_horizontal = ['tags']
    list_display = ('title', 'post_photo', 'slug', 'time_create', 'is_published')
    list_editable = ('slug', 'is_published')
    actions = ('publish_post', 'unpublish_post')
    save_on_top = True

    @admin.action(description='Publish')
    def publish_post(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'Number of posts published: {count}.')

    @admin.action(description='Unpublish')
    def unpublish_post(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'Number of posts unpublished: {count}.', messages.WARNING)

    @admin.display(description='Post photo preview')
    def post_photo(self, post: Post):
        if post.main_photo:
            return mark_safe(f'<img src="{ post.main_photo.url }" width="50">')
        return 'No photo'


@admin.register(PostTag)
class TagAdmin(admin.ModelAdmin):
    fields = ('tag_name', 'tag_slug')
    prepopulated_fields = {'tag_slug': ('tag_name', )}