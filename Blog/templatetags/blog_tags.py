from django import template

from Blog.services import get_all_tags, get_all_authors

register = template.Library()


@register.inclusion_tag('Blog/tag_list.html')
def show_tag_list():
    return {'blog_tags': get_all_tags()}


@register.inclusion_tag('Blog/author_list.html')
def show_author_list():
    return {'blog_authors': get_all_authors()}
