from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.views.generic.edit import FormView
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalFormView

from Shop.forms import CreateProductForm, EditProductForm, ProductImagesForm, CartAdditionForm
from Shop.models import Product, Cart
from django.shortcuts import render

# Create your views here.
from Shop.services import link_product_photo_to_product, get_published_products, get_product_by_seller, \
    get_all_products, add_to_cart, get_product_by_slug, get_products_in_cart, get_cart_by_user, get_cart_sum, \
    clear_cart, delete_product_from_cart, get_available_products


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


class SellerPage(ListView):
    template_name = 'Shop/Shop.html'
    paginate_by = 8
    extra_context = {
        'title': "Edit your products"
    }
    allow_empty = False

    def get_queryset(self):
        return get_product_by_seller(get_all_products(), self.request.user.pk)


class CartEntryCreator(LoginRequiredMixin, BSModalCreateView):
    template_name = 'Shop/Cart_Addition.html'
    form_class = CartAdditionForm
    success_message = 'Product added to the cart'
    success_url = reverse_lazy('shop_main')

    def get_queryset(self):
        return get_product_by_slug(get_published_products(), self.kwargs['slug'])

    def form_valid(self, form):
        form.instance.customer_id = self.request.user.pk
        _object = self.get_object()
        form.instance.product = _object
        if form.instance.quantity > _object.product_quantity:
            form.instance.quantity = _object.product_quantity
        if form.instance.quantity < 1:
            form.instance.quantity = 1
        return super().form_valid(form)


class CartView(LoginRequiredMixin, ListView):
    template_name = 'Shop/Cart.html'
    model = Cart
    extra_context = {'title': 'Cart', 'cart_sum': ''}

    def get_queryset(self):
        res = get_cart_by_user(self.request.user)
        self.extra_context['cart_sum'] = get_cart_sum(res)
        return res


class CartClearView(LoginRequiredMixin, BSModalFormView):
    model = Cart
    template_name = 'Shop/Cart_clear.html'
    success_url = reverse_lazy('shop_main')
    form_class = CartAdditionForm

    def post(self, request, *args, **kwargs):
        clear_cart(user=request.user.pk)
        return super().post(request, *args, **kwargs)


def delete_cart_entry_view(request, pk):
    delete_product_from_cart(cart_pk=pk, user=request.user)
    return redirect('cart')


def edit_cart_view(request):
    pass


