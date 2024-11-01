from django.contrib import admin
from users.models import User
from products.admin import CartAdmin
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    inlines = [CartAdmin]
