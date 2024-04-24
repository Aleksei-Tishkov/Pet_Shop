from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Blog import views
from Blog.views import BlogViewSet

from Pet_Shop import settings

router = DefaultRouter()
router.register('posts', BlogViewSet, basename='spa_posts')

urlpatterns = [
    path('blog/', views.BlogView.as_view(), name='blog_main'),
    path('blog/add_post/', views.AddPost.as_view(), name='add_post'),
    path('blog/add_tag/', views.AddTag.as_view(), name='add_tag'),
    path('blog/delete_post/<slug:slug>/', views.DeletePostView.as_view(), name='delete_post'),
    path('blog/editorial/', views.AuthorPage.as_view(), name='editorial'),
    path('blog/editorial/<slug:slug>/', views.AuthorPostView.as_view(), name='view_post'),
    path('blog/edit_post/<slug:slug>/', views.EditPost.as_view(), name='edit_post'),
    path('blog/tag/<slug:tag_slug>/', views.TagView.as_view(), name='tag'),
    path('blog/author/<slug:author>', views.AuthorView.as_view(), name='post_authors'),
    path('blog/<slug:slug>/', views.PostView.as_view(), name='read_post'),
    path('spa/blog/', include(router.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)