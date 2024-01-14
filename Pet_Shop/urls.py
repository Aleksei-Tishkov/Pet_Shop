from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from Pet_Shop.views import page_not_found, server_error, permission_error, request_error, change_theme_view
from Blog.models import Post, PostTag
from django.contrib.sitemaps.views import sitemap
from Pet_Shop.sitemaps import sitemaps


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include("debug_toolbar.urls")),
    path('', include('Home_Page.urls')),
    path('', include('Shop.urls')),
    path('', include('Blog.urls')),
    path('', include('User.urls', namespace='User')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('sitemap.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('change_theme/', change_theme_view, name='change_theme'),

]

handler404 = page_not_found
handler500 = server_error
handler403 = permission_error
handler400 = request_error

admin.site.site_header = 'Pet_Shop Administration'
admin.site.index_header = 'Pet_Shop Administration'

