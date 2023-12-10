import requests
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


menu = [{'title': "Kinopoisk +", 'url_name': 'home'},
        {'title': "Movies", 'url_name': 'home'},
        {'title': "Categories", 'url_name': 'home'},
        {'title': "Contacts", 'url_name': 'home'},
        {'title': "About us", 'url_name': 'home'}
        ]

paginator = None
result_title = ''


def index(request):
    return render(request, 'home.html',
                  context={'title': 'Кинопоиск +', 'menu': menu})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<center><h1>Страница не найдена</h1></center>')

# получили все фильмы -> [{ movie1 }, { movie2 } и т.д.] и разбили по страницам ->page_obj -> [[{ movie1 }, { movie2 }], [следющие 50 фильмов] ...]
def searchresultsview(request):
    global paginator
    global result_title
    result_title = request.GET.get('s')
    data = []
    try:
        try:
            i = 1
            while True: # можно просто добавить запрос к БД
                response = requests.get(
                    'https://www.omdbapi.com/?apikey=23f82659&s=' + result_title
                    + f'&page={i}')
                if response.status_code == 200:
                    data += response.json()['Search'] # [ {movie1 }, { movie2} ... ] - вообще все
                    i += 1
        except:
            paginator = Paginator(data, 50) # разбили по страницам ->page_obj -> [[{ movie1 }, { movie2 }], [следющие 50 фильмов] ...]
            page_obj = paginator.get_page(1) # [ {movie1 }, { movie2} ... ]
            print(paginator)
            print(page_obj)
            return render(request, 'home.html', 
                          context={'page_obj': page_obj,
                                   'title': 'Кинопоиск +',
                                   'menu': menu, 
                                   'result_title': result_title})
    except:
        return pageNotFound()

#  по страницам ->page_obj -> [[{ movie1 }, { movie2 }], [следющие 50 фильмов] ...]
def show_page(request):
    page_number = int(request.GET.get('page'))
    page_obj = paginator.get_page(page_number) # получаем индекс следующего списка с 50 фильмами -> [следющие 50 фильмов]
    return render(request, 'home.html', context={'page_obj': page_obj,
                  'title': 'Кинопоиск +', 'menu': menu,
                  'result_title': result_title})


def about_movie(request):
    movie_id = request.GET.get('i')
    response = requests.get(
        'https://www.omdbapi.com/?apikey=23f82659&plot=full' +
              f'&i={movie_id}')
    if response.status_code == 200:
        jsn = response.json()
        return render(request, 'about_movie.html', 
                      context={'Title': jsn['Title'], 'Year': jsn['Year'],
                     'Poster': jsn['Poster'], 'Plot': jsn['Plot'], 
                     'menu': menu})
    else:
        return pageNotFound()
