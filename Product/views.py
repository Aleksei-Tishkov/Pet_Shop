from django.shortcuts import render

# Create your views here.
def create_product(request):
    if request.method == 'GET':
        return render(request, 'Products/create_product.html')