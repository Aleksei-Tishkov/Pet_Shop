from django.contrib import admin, messages

from Product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'quantity', 'is_published', 'product_type')
    list_display_links = ('product_name', )
    list_editable = ('price', 'quantity', 'is_published')
    search_fields = ('product_name', 'description')
    list_filter = ('product_type', )
    actions = ('publish_product', 'unpublish_product')

    @admin.action(description='Publish')
    def publish_product(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f'Number of products published: {count}.')

    @admin.action(description='Unpublish')
    def unpublish_product(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f'Number of products unpublished: {count}.', messages.WARNING)