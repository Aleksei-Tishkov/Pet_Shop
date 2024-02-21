from Blog.models import Post, PostTag


def get_all_posts():
    return Post.objects.all()


def get_published_posts():
    return Post.objects.filter(is_published=True).select_related('author')


def get_all_tags():
    return PostTag.objects.all()


def get_post_tags():
    return PostTag.objects.all()


def get_tag(model, instance):
    return model.objects.get(tag_slug=instance.kwargs['tag_slug'])


def get_author(model, instance):
    return model.objects.get(user_slug=instance.kwargs['author'])


def get_all_authors():
    return get_published_posts().order_by().distinct('author')


def get_posts_by_tag(queryset, tag):
    return queryset.filter(tags__tag_slug=tag).select_related('author')


def get_products_by_related_post(queryset, post):
    return


def get_posts_by_author(queryset, author):
    return queryset.filter(author__user_slug=author)


def get_post_by_pk(model, pk):
    return model.objects.filter(pk=pk)
