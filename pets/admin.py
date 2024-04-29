from django.contrib import admin

from .models import Product, Category, Animal




admin.site.index_title = "Зоомагазин верный друг"

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')
