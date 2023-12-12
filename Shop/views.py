from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView

from Shop.forms import CreateProductForm, EditProductForm
from Shop.models import Product
from django.shortcuts import render

# Create your views here.


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
    success_url = reverse_lazy('home')
    template_name = 'Shop/Product_create.html'
    extra_context = {'title': 'Edit your product'}

    def get(self, request, *args, **kwargs):
        __object = self.get_object()
        if __object.product_seller != request.user:
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)
