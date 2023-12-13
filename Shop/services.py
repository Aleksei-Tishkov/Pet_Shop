from Shop.models import ProductPhoto


def publish_prod(queryset):
    queryset.update(product_is_published=True)


def unpublish_prod(queryset):
    queryset.update(product_is_published=False)


def link_product_photo_to_product(product, product_photo):
    ProductPhoto.objects.create(product=product, product_photo=product_photo)
