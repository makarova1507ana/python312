from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from .models import Product, Category, Pet
from feedback.models import Feedback

#
# def index(request):
#
#     return render(request, "index.html")

class Home(TemplateView):
    template_name = 'index.html'
    extra_context = {'name_product': 'name1',
                     'products': Product.objects.filter(amount=1)[:3]}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedbacks = Feedback.objects.filter(rating=5) # [Feedback(...,product), ...]
        products_highest_mark = set()
        for feedback in feedbacks:
            product_id = feedback.product.id #  feedback.product -> title
            product = Product.objects.get(id=product_id)
            products_highest_mark.add(product)
        context['products_highest_mark'] = products_highest_mark
        return context

# def catalog(request):
#
#     pets = Pet.objects.all()
#     results = Product.objects.all().order_by('id')
#     data = {
#         'pets': pets,
#         "products": results
#     }
#
#     return render(request,"catalog.html",  context=data)
class Catalog(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'  # 'products' - это ключ словаря
    def get_queryset(self):
           # Получаем список книг, отсортированный по дате публикации
           return Product.objects.all()

    def get_context_data(self, **kwargs):
        # Дополнительные данные для передачи в контекст (необязательно)
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.all()
        return context

# def categories(request, slug):
#     try:
#         pets = Pet.objects.all()
#         category = Pet.objects.get(slug=slug)
#
#         results = Product.objects.filter(category=category.id)
#         data = {
#             'pets': pets,
#             'category': category.title,
#             "products": results
#         }
#         return render(request,"products.html",context=data)
#     except:
#         return render(request, '404.html', status=404)

class Category_Products(ListView):
    model = Category
    template_name = 'products.html'
    context_object_name = 'categories'  # 'products' - это ключ словаря


    def get_context_data(self, **kwargs):
        # Дополнительные данные для передачи в контекст (необязательно)
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.all()

        pet = Pet.objects.get(slug=self.kwargs['slug'])
        categories = Category.objects.filter(pet=pet.id)
        products = Product.objects.filter(category=pet.id)
        context['pets'] = pets
        context['pet'] = pet
        context['categories'] = categories
        context['products'] = products

        return context
#
# def show_product(request, product_id):
#     try:
#         product = Product.objects.get(id=product_id)
#         feedbacks = product.feedback_set.all()
#         data = {
#             "product": product,
#             'feedbacks': feedbacks
#         }
#         return render(request,"product.html",context=data)
#     except:
#         return render(request, '404.html', status=404)
class Product_Detail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'  # Имя переменной в URL для первичного ключа