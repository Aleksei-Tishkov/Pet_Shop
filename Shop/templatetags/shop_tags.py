from django import template

from Shop.services import *

register = template.Library()


@register.inclusion_tag('Shop/Product_categories.html')
def category_list():
    return {'product_categories': get_all_categories()}

@register.filter
def multiply(value, arg):
    return value * arg