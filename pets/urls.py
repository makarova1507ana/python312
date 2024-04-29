from django.urls import path, re_path

import pets.views as pets

urlpatterns = [
    path('', pets.index, name="main_url"),
    path('pet/<slug:pet_name>/', pets.pet, name="pet"),

    path("products/<slug:cat_name>/", pets.show_products, name="products"),
    path("product/<int:product_id>/", pets.show_product, name="product"),
]