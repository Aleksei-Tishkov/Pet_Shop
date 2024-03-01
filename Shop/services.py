import datetime
import re
from collections import defaultdict

from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

from Pet_Shop import settings
from Shop.models import Product, ProductPhoto, Cart, Order
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


def get_available_products():
    return get_published_products().filter(product_quantity__gt=0)


def get_product_by_seller(queryset, seller):
    return queryset.filter(product_seller_id=seller)


def add_to_cart(customer: User, product: Product, quantity: int) -> None:
    Cart.objects.create(customer_id=customer.pk,
                        product_id=product.pk,
                        quantity=quantity,
                        customer_postalcode=customer.user_postalcode,
                        customer_address=customer.user_address)


def get_product_by_slug(queryset, slug):
    return queryset.filter(slug=slug)


def get_cart_by_user(user):
    return Cart.objects.filter(customer_id=user)


def add_address_to_cart(user, postal_code, address):
    cart = get_cart_by_user(user)
    cart.update(customer_postalcode=postal_code, customer_address=address)

    # cart = get_cart_by_user(user)
    # for obj in cart:
    # obj.customer_postalcode = postal_code
    # obj.customer_address = address


def get_products_in_cart(user):
    return Product.objects.filter(pk__in=Cart.objects.filter(customer_id=user).values_list('product_id'))


def get_cart_sum(cart):
    res = 0
    for o in cart:
        res += o.quantity * o.product.product_price
    return res


def get_cart_entry_by_pk(pk):
    return Cart.objects.get(pk=pk)


def delete_product_from_cart(cart_pk, user) -> None:
    try:
        product = get_cart_entry_by_pk(cart_pk)
        if product.customer == user:
            product.delete()
    except ObjectDoesNotExist:
        return


def clear_cart(user) -> None:
    get_cart_by_user(user).delete()


def process_cart(string: str) -> None:
    user = int(re.search(r'(?<==)(?:\d+)', string)[0])
    cart = get_cart_by_user(user)
    customer_postalcode = cart[0].customer_postalcode
    customer_address = cart[0].customer_address
    pushes = defaultdict(list)
    for c in cart:
        product = Product.objects.get(pk=c.product.pk)
        product_quantity = c.quantity
        if product.product_quantity - product_quantity < 0:
            return
        product.product_quantity -= product_quantity
        product.save()                                  # Updates product quantity in stock
        seller = c.product.product_seller
        pushes[seller].append(f'{c.quantity} {c.product}')
        Order.objects.create(seller=seller,
                             customer=c.customer,
                             product=c.product,
                             quantity=c.quantity,
                             customer_postalcode=c.customer_postalcode,
                             customer_address=c.customer_address)
        c.delete()
    for seller in pushes:
        send_mail(subject="PetShop. New purchase",
                  message=f'Hello!\nYou have a new purchase via PetShop!\n{cart[0].customer.username} just bought ' +
                          ', '.join(pushes[seller]) +
                          f'.\nThe purchase must be shipped to {customer_postalcode}, {customer_address}' +
                          f' till {(datetime.datetime.now() + datetime.timedelta(days=7)).date()}.\nThank you!',
                  recipient_list=[seller.email],
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  fail_silently=False,
                  )



def delete_address(cart):
    cart.update(customer_postalcode=None, customer_address=None)
