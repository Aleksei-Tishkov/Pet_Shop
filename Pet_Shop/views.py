from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'page_404.html', status=404)


def server_error(request):
    return render(request, 'page_500.html', status=500)


def permission_error(request, exception):
    return render(request, 'page_403.html', status=403)


def request_error(request, exception):
    return render(request, 'page_400.html', status=400)