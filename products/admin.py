from django.contrib import admin

from products.models import Product, ProductCategory, Cart


# Register your models here.

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity','category')
    fields = ('name', 'description',('price', 'quantity'), 'image','category')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)


class CartAdmin(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0


