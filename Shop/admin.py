from django.contrib import admin, messages
from Shop.services import publish_prod, unpublish_prod
from Shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('product_name', 'slug', 'product_price', 'product_quantity', 'product_is_published',
              'product_type', 'related_post', 'product_seller'
              )
    list_display = ('product_name', 'product_price', 'product_quantity', 'product_is_published', 'product_type',
                    'product_seller',)
    prepopulated_fields = {'slug': ('product_name', )}
    list_display_links = ('product_name', )
    list_editable = ('product_price', 'product_quantity', 'product_is_published')
    search_fields = ('product_name', 'product_description')
    list_filter = ('product_type', )
    actions = ('publish_product', 'unpublish_product')

    @admin.action(description='Publish')
    def publish_product(self, request, queryset):
        count = publish_prod(queryset)
        self.message_user(request, f'Number of products published: {count}.')

    @admin.action(description='Unpublish')
    def unpublish_product(self, request, queryset):
        count = unpublish_prod(queryset)
        self.message_user(request, f'Number of products unpublished: {count}.', messages.WARNING)