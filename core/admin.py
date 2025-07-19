from django.contrib import admin
from .models import Categories, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'description', 'image', 'price', 'created']