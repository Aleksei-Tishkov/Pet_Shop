from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def post_list(request):
    return render(request, 'blog/index.html')