from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

# def cats(request):
#     return HttpResponse("<h2>Коты</h2>")
#
# def dogs(request):
#     return HttpResponse("<h2>Собаки</h2>")
#
class Cat:
    def __init__(self):
        self.name = "Cat"
        self.age = 3

    # def __repr__(self):
    #     return f"name: {self.name}, age: {self.age}"
def pet(request, pet_slug):
    data = {
        "pet_name": pet_slug,
        "pet_text": "Это текст про страницу с животными",
        "pet_list": ["Кот", "Собака"],
        "pet_int": 34,
        "pet_dict": {"cat": "Кот", "dog": "Собака"},
        "pet_obj": Cat()
    }
    # будем делать обращение к БД " существует ли pet_slug ?"
    if pet_slug in ['cats', 'dogs']:
        return render(request, "pet_page.html", context=data) # context преобразует все к строке
    #return HttpResponseNotFound(f"<h2>ОШИБКА!!! Нет такой страницы!</h2><img src='https://i.pinimg.com/736x/c9/e3/eb/c9e3eb487b0deb3f50501c196e332b58.jpg'>") # будет отправлен статус код 404
    return render(request, "pageNotFound404.html", status=404)

def petGET(request):
    title = request.GET.get('title')# лучше примернять когда есть форма
    return HttpResponse(f"<h2>{title}</h2>")



def categories(request, categorie_id):
    return HttpResponse(f"<h2>Категории</h2><p>id:{ categorie_id }</p>")