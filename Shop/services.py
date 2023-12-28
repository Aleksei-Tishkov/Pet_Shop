from Shop.models import Product, ProductPhoto, Cart
from User.models import User
from django.db.models import Sum


def publish_prod(queryset):
    queryset.update(product_is_published=True)


def unpublish_prod(queryset):
    queryset.update(product_is_published=False)


def link_product_photo_to_product(product, product_photo):
    ProductPhoto.objects.create(product=product, product_photo=product_photo)


def get_all_products():
    return Product.objects.all()


def get_published_products():
    return Product.objects.filter(product_is_published=True).select_related('product_seller')


def get_product_by_seller(queryset, seller):
    return queryset.filter(product_seller_id=seller)


def add_to_cart(customer: User, product: Product, quantity: int) -> None:
    Cart.objects.create(customer_id=customer.pk, product_id=product.pk, quantity=quantity)


def get_product_by_slug(queryset, slug):
    return queryset.filter(slug=slug)


def get_cart_by_user(user):
    if not user:
        raise
    return Cart.objects.filter(customer_id=user)


def get_products_in_cart(user):
    return Product.objects.filter(pk__in=Cart.objects.filter(customer_id=user).values_list('product_id'))


def get_cart_sum(cart):
    res = 0
    for o in cart:
        res += o.quantity * o.product.product_price
    return res
