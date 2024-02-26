from django.conf.urls.static import static
from django.urls import path, include

from Blog.models import Post
from Pet_Shop import settings
from Search import views
from Shop.models import Product

app_name = 'search'

urlpatterns = [
    path('', views.SearchView.as_view(), name='search_main'),
    path('search_results/posts/<str:search>',
         views.PostSearchResults.as_view(queryset=Post.objects.all()),
         name='posts_search_results'),
    path('search_results/products/<str:search>',
         views.ProductSearchResults.as_view(queryset=Product.objects.all()),
         name='products_search_results'),

]

