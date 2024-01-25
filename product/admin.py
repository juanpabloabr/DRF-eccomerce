from django.contrib import admin

from .models import (
    Supplier,
    Category,
    Product,
    Review,
)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','SKU','supplier','category','description','created','updated')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product','user_name','email','review','rating','created','updated')