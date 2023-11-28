from django.conf.urls.static import static
from django.urls import path, include
from Blog import views

from Pet_Shop import settings


urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog_main'),
    path('blog/add_post/', views.AddPost.as_view(), name='add_post'),
    path('blog/add_tag/', views.AddTag.as_view(), name='add_tag'),
    path('blog/edit_post/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('blog/<slug:slug>/', views.PostView.as_view(), name='post'),
    path('blog/tag/<slug:tag_slug>/', views.TagView.as_view(), name='tag'),
    path('blog/author/<slug:author>', views.AuthorView.as_view(), name='post_authors'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)