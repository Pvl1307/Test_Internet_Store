from django.contrib import admin

from store.models import Category, SubCategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Административный класс для модели Category"""
    list_display = ('name', 'slug_name', 'image',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Административный класс для модели SubCategory"""
    list_display = ('category', 'name', 'slug_name', 'image',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Административный класс для модели Product"""
    list_display = ('subcategory', 'name', 'slug_name', 'image_small', 'image_medium', 'image_large', 'price',)
