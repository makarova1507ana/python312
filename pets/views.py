from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("<h2>Главная <a href='http://127.0.0.1:8000/pets/cats/'>Коты</a> Собаки</h2>")

# def cats(request):
#     return HttpResponse("<h2>Коты</h2>")
#
# def dogs(request):
#     return HttpResponse("<h2>Собаки</h2>")
#
def pet(request, pet_slug):
    # будем делать обращение к БД " существует ли pet_slug ?"
    if pet_slug in ['cats', 'dogs']:
        return HttpResponse(f"<h2>{pet_slug}</h2>")
    return HttpResponseNotFound(f"<h2>ОШИБКА!!! Нет такой страницы!</h2><img src='https://i.pinimg.com/736x/c9/e3/eb/c9e3eb487b0deb3f50501c196e332b58.jpg'>") # будет отправлен статус код 404


def petGET(request):
    title = request.GET.get('title')# лучше примернять когда есть форма
    return HttpResponse(f"<h2>{title}</h2>")



def categories(request, categorie_id):
    return HttpResponse(f"<h2>Категории</h2><p>id:{ categorie_id }</p>")