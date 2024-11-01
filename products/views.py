from itertools import product

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product, ProductCategory, Cart


# Create your views here.

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page_number=1):

    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Products',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,

    }
    return render(request, 'products/products.html', context)

def cart(request):
    carts = Cart.objects.filter(user=request.user)

    context = {
        'title': 'Cart',
        'carts': carts,

    }
    return render(request, 'products/cart.html', context)

@login_required
def add_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart_product = carts.first()
        cart_product.quantity += 1
        cart_product.save()

    return redirect(request.META['HTTP_REFERER'])

@login_required
def delete_cart(request, cart_id):
    cart_product = Cart.objects.get(pk=cart_id)
    cart_product.delete()
    return redirect(request.META['HTTP_REFERER'])