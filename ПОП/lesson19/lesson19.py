# # import requests
# # from datetime import datetime, timedelta
# # import os
# # def download_image(url, file_name):
# #     response = requests.get(url)
# #     if response.status_code == 200: # status_code == 200, потому что ожидаем ПОЛУЧИТЬ изображение
# #         with open(file_name, 'wb') as file: # wb - запись бинарного файла
# #             file.write(response.content) # запись самой картинки
# #             print(f"Изображение скачано как '{file_name}'")
# #     else:
# #         print("Не удалось скачать изображение")
# #
# # # # Укажите ссылку на изображение и имя файла, в который нужно сохранить
# # # image_url = 'https://apod.nasa.gov/apod/image/2304/hubble_ngc2419_potw1908a.jpg'#'https://example.com/image.jpg'
# # # date = datetime.datetime.now()
# # # date = date.strftime("%m-%d-%Y-%H-%M-%S")
# # #
# # # if not os.path.exists("uploads"):  #  если не существует папка
# # #     os.mkdir("uploads") # создаем папку
# # #
# # #
# # # file_name = f'uploads/{date}.jpg'
# # #
# # # download_image(image_url, file_name)
# #
# #
# # # #—------------------------------- Задача —--------------------------------#
# # # скачать изображения найденные за последние три дня в папку uploads
# #
# # # 1 понять как взять текущей день
# # # 2 как взять день 3 дня назад
# #
# # #  как сформировать и отправить запрос
# # #  отправить запрос и получить json файла
# #
# # #  надо вытащить изображения
# # # и отправить запрос на скачивание
# #
# #
# #
# #
# # # 1 понять как взять текущей день
# # # 2 как взять день 3 дня назад
# #
# #
# # date = datetime.now() # специльный объект "datetime"
# # date = date.strftime("%m-%d-%Y-%H-%M-%S") # для имени нашего изображения
# # start_date = datetime.now() - timedelta(days=2)
# # start_date ="&start_date="+start_date.strftime("%Y-%m-%d") # для параметра start_date запроса
# # end_date = "&end_date="+ datetime.now().strftime("%Y-%m-%d")# для параметра start_date запроса
# # # print(start_date)
# # # print(end_date)#date.strftime("%d-%m-%Y-%H-%M-%S")) # (date.strftime("%m-%d-%Y-%H-%M-%S") -> строка заданного формата
# #
# # #  как сформировать и отправить запрос
# # #  отправить запрос и получить json файла
# #
# # api_key = "?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla"
# # url = f"https://api.nasa.gov/planetary/apod{api_key}{start_date}{end_date}"
# # #  requests.get(url) - отправка запроса
# # # response =  ответ то, что вернул -> requests.get(url)
# # response = requests.get(url) # response -> .json
# # #print(response.json())  # response.json() -> [{},{},{}]
# #
# #
# #
# #
# # count = 0
# # for request in response.json(): # request -> {'date': 'value', и т.д.}
# #     if request['media_type'] == 'image':
# #         #  надо вытащить изображения
# #         # и отправить запрос на скачивание
# #         # print(request['url']) # здесь ссылка на изображение
# #         image_url = request['url']
# #
# #         if not os.path.exists("uploads"):  #  если не существует папка
# #             os.mkdir("uploads") # создаем папку
# #         count += 1
# #         file_name = f'uploads/image{count}_{date}.jpg'
# #
# #         download_image(image_url, file_name)
# #     else:
# #         print("this is video :(")
# #
#
# # Доп задание
# # удалить папку "uploads" с файлами
# import os
# command = input("""
# 1. удалить папку "uploads"
# 2. выйти из программы
# """)
#
# if command == "1":
#     if os.path.exists("uploads"):  # если существует папка
#         files = os.listdir("uploads")
#         os.chdir('uploads')
#
#         # перебрать все файлы и удалить каждый из них
#         for file_name in files:
#             os.remove(file_name)
#
#         os.chdir('../') #возвращаемся на одну папку  выше
#         os.rmdir("uploads")  # создаем папку



#—------------------------------- Задача —--------------------------------#
# https://jsonplaceholder.typicode.com/
# https://jsonplaceholder.typicode.com/posts
import requests
# дано название статьи ->  показать имя пользователя, название статьи и текст статьи
#  posts = requests.get(https://jsonplaceholder.typicode.com/posts).json()  -> все статьти [{}, {}, {}]
#  для каждой статьи (for post)
#    if данное название статьи == post["title"]
#       title = post["title"] -> название статьи
#       content = post["body"] -> текст статьи
#       id_user = post["userId"]
# def find_post(title_for_search):
#     url = "https://jsonplaceholder.typicode.com/posts"
#     posts = requests.get(url).json()  # [{}, {}, {}] # отправляем запрос на получение файла
#     for post in posts:
#         if post['title'] == title_for_search:
#             title = post["title"] # -> название статьи
#             content = post["body"] # -> текст статьи
#             id_user = post["userId"]
#             autor = find_name_user(id_user) #находим имя пользователя
#             return (autor, title, content)
#     return ("None", "None", "None")
#
#
# # показать имя пользователя
# # https://jsonplaceholder.typicode.com/users [{}, {}]
# #  для каждой пользователя (for user)
# #    if id_user == user["id"]
# #       name = user["name"] -> имя пользователя
# def find_name_user(id_user):
#     url = "https://jsonplaceholder.typicode.com/users"
#     users = requests.get(url).json()  # [{}, {}, {}]
#     for user in users:
#         if user['id'] == id_user:
#             name = user["name"]
#             return name
#     return "None"
#
# # показать имя
# post = find_post("sunt au facere repellat provident occaecati excepturi optio reprehenderit")
# print(f"name: {post[0]} \ntitle: {post[1]} \ncontent: {post[2]}")

# ------------------------------------------------------------2 ---------------------------#
def find_post(id_post):
    url = f"https://jsonplaceholder.typicode.com/posts/?id={id_post}"
    response = requests.get(url) # отправляем запрос на получение файла
    if response.status_code == 200:
        post = response.json() # {}
        title = post[0]["title"] # -> название статьи
        content = post[0]["body"] # -> текст статьи
        id_user = post[0]["userId"]
        autor = find_name_user(id_user) #находим имя пользователя
        return (autor, title, content)
    return ("None", "None", "None")

def find_name_user(id_user):
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)  # отправляем запрос на получение файла
    if response.status_code == 200:
        user = requests.get(url+f"/?id={id_user}").json() # {}
        name = user[0]["name"]
        return name
    return "None"


post = find_post("1")
print(f"name: {post[0]} \ntitle: {post[1]} \ncontent: {post[2]}")