from django.db import models
from users.models import User

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Название: {self.name} | Категория: {self.category} | Цена: {self.price} | Количество: {self.quantity}"

class CartQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(cart.sum() for cart in self)

    def total_quantity(self):
        return sum(cart.quantity for cart in self)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartQuerySet.as_manager()

    def __str__(self):
        return f"Корзина {self.user.username} | Продукт: {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity

