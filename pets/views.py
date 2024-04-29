from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Animal, Product, Category


def index(request):
    animals = Animal.objects.all()
    data ={
        'animals': animals
    }

    return render(request, "index.html", data)


def pet(request, pet_name):
    # вместо try    -> get_object_or_404(Animal,slug=pet_name ) # obj  or 404 , но надо добавить представление обратки 404
    try:
        animal = Animal.objects.get(slug=pet_name)
        categories = animal.category_set.all()

        data = {
           'title': animal.title,
            'categories': categories
        }
        return render(request, "pet_page.html", context=data) # context преобразует все к строке
    except:
        return render(request, "pageNotFound404.html", status=404)




def show_products(request, cat_name):
    category = Category.objects.get(slug=cat_name)
    results = Product.objects.filter(category=category.id)
    data = {
        'category': category.title,
        "products": results
    }
    return render(request,"products.html",context=data)


def show_product(request, product_id):
    product = Product.objects.get(id=product_id)
    feedbacks = product.feedback_set.all()
    data = {
        "product": product,
        'feedbacks': feedbacks
    }
    return render(request,"product.html",context=data)
