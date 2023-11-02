from django.conf.urls.static import static
from django.urls import path, include
from Blog import views

from Pet_Shop import settings

urlpatterns = [
    path('blog/', views.blog_view, name='blog_main'),
    path('blog/add_post/', views.add_post, name='add_post'),
    path('blog/<slug:slug>/', views.post_view, name='post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)