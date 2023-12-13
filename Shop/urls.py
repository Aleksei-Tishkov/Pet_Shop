from django.conf.urls.static import static
from django.urls import path, include

from Pet_Shop import settings
from Shop import views

urlpatterns = [
    path('shop/', views.ShopView.as_view(), name='shop_main'),
    path('shop/add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('shop/edit_product/<slug:slug>/', views.EditProductView.as_view(), name='edit_product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)