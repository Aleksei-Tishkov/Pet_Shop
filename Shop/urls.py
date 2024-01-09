from django.conf.urls.static import static
from django.urls import path, include

from Pet_Shop import settings
from Shop import views
from Shop.views import CartEntryDeleter

urlpatterns = [
    path('shop/', views.ShopView.as_view(), name='shop_main'),
    path('shop/add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('shop/editorial/', views.SellerPage.as_view(), name='shop_editorial'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('shop/edit_product/<slug:slug>/', views.EditProductView.as_view(), name='edit_product'),
    path('shop/product/<slug:slug>/', views.ProductView.as_view(), name='product_view'),
    path('shop/add_to_cart/<slug:slug>/', views.CartEntryCreator.as_view(), name='add_to_cart'),
    path('cart/clear_cart/', views.CartClearView.as_view(), name='clear_cart'),
    path('cart/delete/<int:pk>/', views.delete_cart_entry, name='cart_delete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)