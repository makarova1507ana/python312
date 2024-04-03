from django.urls import path, re_path

import pets.views as pets

urlpatterns = [
    path('', pets.index, name="main_url"), #  pets = http://127.0.0.1:8000/pets/
    path('petGET/', pets.petGET),  # http://127.0.0.1:8000/pets/petGET/
    path('feedback/', pets.feedback),
    path('<slug:pet_slug>/', pets.pet), # http://127.0.0.1:8000/pets/{pet_slug}/
    path('categories/<int:categorie_id>/', pets.categories), # http://127.0.0.1:8000/pets/categories/{int}/
]