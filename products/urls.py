
from django.urls import path
from products.views import index, products, cart, add_cart, delete_cart
app_name = 'products'
urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('cart/', cart, name='cart'),
    path('cart/add/<int:product_id>/', add_cart, name='add_cart'),
    path('cart/delete/<int:cart_id>/', delete_cart, name='delete_cart'),

]
