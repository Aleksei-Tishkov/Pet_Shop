from Shop.models import Product, ProductPhoto


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


