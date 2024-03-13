from django.urls import path, re_path

import pets.views as pets

urlpatterns = [
    path('pets/', pets.index), # http://127.0.0.1:8000/pets/
]