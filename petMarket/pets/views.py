from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import  Product, Category, Pet


def index(request):

    return render(request, "index.html")


def catalog(request):

    pets = Pet.objects.all()
    results = Product.objects.all().order_by('id')
    data = {
        'pets': pets,
        "products": results
    }

    return render(request,"catalog.html",  context=data)




def categories(request, slug):
    try:
        pets = Pet.objects.all()
        category = Pet.objects.get(slug=slug)

        results = Product.objects.filter(category=category.id)
        data = {
            'pets': pets,
            'category': category.title,
            "products": results
        }
        return render(request,"products.html",context=data)
    except:
        return render(request, '404.html', status=404)

def show_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        feedbacks = product.feedback_set.all()
        data = {
            "product": product,
            'feedbacks': feedbacks
        }
        return render(request,"product.html",context=data)
    except:
        return render(request, '404.html', status=404)
