from django.urls import path, re_path

import pets.views as pets

urlpatterns = [
    path('', pets.index, name="main_url"),
    path('catalog/', pets.catalog, name="catalog"),

    path("categories/<slug:slug>/", pets.categories, name="categories"),
    path("product/<int:product_id>/", pets.show_product, name="product"),
]