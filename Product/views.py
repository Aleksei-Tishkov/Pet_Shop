from django.shortcuts import render, get_object_or_404
from Product.models import Product
from django.shortcuts import render

# Create your views here.


def create_product(request):
    if request.method == 'GET':
        return render(request, 'Product/Product_create.html')


def product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    data = {
        'product_name': product.product_name,
        'product_type': product.product_type,
        'product_description': product.description,
        #'product_specs': product
    }
    return render(request, 'Product/Product_view.html', context=data)

