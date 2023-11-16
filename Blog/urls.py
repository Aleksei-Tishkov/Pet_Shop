from django.conf.urls.static import static
from django.urls import path, include
from Blog import views

from Pet_Shop import settings

urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog_main'),
    path('blog/add_post/', views.AddPost.as_view(), name='add_post'),
    path('blog/<slug:slug>/', views.PostView.as_view(), name='post'),
    path('tag/<slug:tag_slug>/', views.TagView.as_view(), name='post_tags'),
    path('author/<slug:author>', views.AuthorView.as_view(), name='post_authors'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)