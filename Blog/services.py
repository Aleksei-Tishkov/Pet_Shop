from Blog.models import Post, PostTag


def get_published_posts():
    return Post.objects.filter(is_published=True)



def get_tag(model, instance):
    return model.objects.get(tag_slug=instance.kwargs['tag_slug'])


def get_posts_by_tag(queryset, tag):
    return queryset.filter(tags__tag_slug=tag)

