import uuid

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.views.generic.edit import FormView
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalFormView, BSModalUpdateView
from paypal.standard.forms import PayPalPaymentsForm

from Shop.forms import CreateProductForm, EditProductForm, ProductImagesForm, CartAdditionForm, CartEntryChange, \
    CartDeleteForm, AddressForm
from Shop.models import Product, Cart, ProductTag
from Pet_Shop.settings import PAYPAL_BUSINESS_EMAIL
from django.shortcuts import render

from Shop.services import link_product_photo_to_product, get_published_products, get_product_by_seller, \
    get_all_products, add_to_cart, get_product_by_slug, get_products_in_cart, get_cart_by_user, get_cart_sum, \
    clear_cart, delete_product_from_cart, get_available_products, add_address_to_cart, delete_address, get_product_tag, \
    get_products_by_tag


class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateProductForm
    template_name = 'Shop/Product_create.html'
    extra_context = {'title': 'Add a new product'}

    def form_valid(self, form):
        form.instance.product_seller = self.request.user
        form.instance.product_slug = slugify(self.request.POST['product_name'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('edit_product', args=(self.object.slug,))


class EditProductView(UpdateView):
    model = Product
    form_class = EditProductForm
    success_url = reverse_lazy('shop_main')
    template_name = 'Shop/Product_create.html'
    image_form = ProductImagesForm()
    extra_context = {'title': 'Edit your product', 'image_form': image_form}

    def get(self, request, *args, **kwargs):
        __object = self.get_object()
        if __object.product_seller != request.user:
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        __object = self.get_object()
        files = request.FILES.getlist('product_photo')
        for file in files:
            link_product_photo_to_product(__object, file)
        return super().post(request, *args, **kwargs)


class ShopView(ListView):
    template_name = 'Shop/Shop.html'
    model = Product
    paginate_by = 8
    extra_context = {'title': 'Shop'}

    def get_queryset(self):
        if self.request.user.is_authenticated:
            self.extra_context['cart'] = get_products_in_cart(self.request.user)
        return get_available_products()


class ProductView(DetailView):
    model = Product
    template_name = 'Shop/Product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        if self.request.user.is_authenticated:
            context['cart'] = get_products_in_cart(self.request.user)
            context.update(kwargs)
        return super().get_context_data(**context)


class ProductTagView(ListView):
    template_name = 'Shop/Shop.html'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_product_tag(ProductTag, self)
        context['title'] = tag.product_tag_name.title()
        return context

    def get_queryset(self):
        return get_products_by_tag(self.kwargs['product_tag_slug'])


class SellerPage(ListView):
    template_name = 'Shop/Shop.html'
    paginate_by = 8
    extra_context = {
        'title': "Edit your products"
    }
    allow_empty = False

    def get_queryset(self):
        return get_product_by_seller(get_all_products(), self.request.user.pk)


class AddProductTag(CreateView):
    model = ProductTag
    fields = '__all__'
    template_name = 'Blog/Add_tag.html'
    success_url = reverse_lazy('shop_main')
    extra_context = {'title': 'Tag addition form'}


class CartEntryCreator(LoginRequiredMixin, BSModalCreateView):
    template_name = 'Shop/Cart_Addition.html'
    form_class = CartAdditionForm
    success_message = 'Product added to the cart'
    success_url = reverse_lazy('shop_main')
    extra_context = {'quantity': 1, 'name': None}

    def get_queryset(self):
        return get_product_by_slug(get_published_products(), self.kwargs['slug'])

    def form_valid(self, form):
        user = self.request.user
        form.instance.customer_id = user.pk
        _object = self.get_object()
        self.quantity = _object.product_quantity
        form.instance.customer_postalcode = user.user_postalcode
        form.instance.customer_address = user.user_address
        form.instance.product = _object
        if form.instance.quantity > self.quantity:
            form.instance.quantity = self.quantity
        if form.instance.quantity < 1:
            form.instance.quantity = 1
        return super().form_valid(form)


class CartEditView(LoginRequiredMixin, BSModalUpdateView):
    model = Cart
    template_name = 'Shop/Cart_Addition.html'
    form_class = CartEntryChange
    success_message = 'Cart was updated.'
    success_url = reverse_lazy('cart')


class CartView(LoginRequiredMixin, ListView):
    template_name = 'Shop/Cart.html'
    model = Cart

    def get_queryset(self):
        cart = get_cart_by_user(self.request.user)
        if not cart:
            return cart
        if cart[0].customer_postalcode and cart[0].customer_address:
            shipping_address = True
        else:
            shipping_address = False
        shipping_customer_postalcode = cart[0].customer_postalcode
        shipping_customer_address = cart[0].customer_address
        cart_sum = get_cart_sum(cart)
        if shipping_address:
            paypal_dict = {
                "business": PAYPAL_BUSINESS_EMAIL,
                "amount": cart_sum,
                "item_name": str(cart),
                "invoice": uuid.uuid4(),
                "notify_url": self.request.build_absolute_uri(reverse('paypal-ipn')),
                "return": self.request.build_absolute_uri(reverse('cart')),
                "cancel_return": self.request.build_absolute_uri(reverse('cart')),
            }
            form = PayPalPaymentsForm(initial=paypal_dict)
        else:
            form = AddressForm()
        self.extra_context = {'title': 'Cart', 'cart_sum': cart_sum, 'form': form,
                              'shipping_address': shipping_address,
                              'shipping_customer_postalcode': shipping_customer_postalcode,
                              'shipping_customer_address': shipping_customer_address}
        return cart

    def get(self, request, *args, **kwargs):
        self.get_queryset()
        return super(CartView, self).get(request, *args, **kwargs)

    def post(self, request):
        print(type(request.POST['customer_postalcode']))
        add_address_to_cart(request.user, request.POST['customer_postalcode'], request.POST['customer_address'])
        return redirect('cart')


class CartClearView(LoginRequiredMixin, BSModalFormView):
    model = Cart
    template_name = 'Shop/Cart_clear.html'
    success_url = reverse_lazy('shop_main')
    form_class = CartDeleteForm

    def post(self, request, *args, **kwargs):
        clear_cart(user=request.user.pk)
        return super().post(request, *args, **kwargs)


def delete_cart_entry_view(request, pk):
    delete_product_from_cart(cart_pk=pk, user=request.user)
    return redirect('cart')


def change_address(request):
    cart = get_cart_by_user(request.user)
    delete_address(cart)
    return redirect('cart')
