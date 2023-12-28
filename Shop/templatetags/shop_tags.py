from django import template

from Shop.services import *

register = template.Library()


@register.inclusion_tag('Shop/Product_categories.html')
def category_list():
    return {'product_categories': None} # get_all_categories (from services)


@register.filter
def multiply(value, arg):
    return value * arg