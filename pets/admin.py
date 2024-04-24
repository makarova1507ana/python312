from django.contrib import admin

from .models import Product, Category, Animal
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Animal)


admin.site.index_title = "Известные женщины мира"
