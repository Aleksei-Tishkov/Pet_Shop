from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from Blog.models import Post
from Search.services import model_filter, queryset_filter
from Shop.models import Product


class SearchView(View):
    template_name = 'Search/Search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('search', None)
        post_search_results = model_filter(Post, query)
        product_search_results = model_filter(Product, query)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'search': query or '',
                'post_search_results': post_search_results[:3],
                'post_search_results_count': post_search_results.count(),
                'product_search_results': product_search_results[:5],
                'product_search_results_count': product_search_results.count(),
            }
        )


class FullSearchResults(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'search': self.request.GET.get('search', None) or '',
            # 'last': self.get_pagination_url()
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.path.split('/')[-1]
        return queryset_filter(queryset, query)


class PostSearchResults(FullSearchResults):
    template_name = 'Search/Search_results_posts.html'
    paginate_by = 4


class ProductSearchResults(FullSearchResults):
    template_name = 'Search/Search_results_products.html'
    paginate_by = 10
