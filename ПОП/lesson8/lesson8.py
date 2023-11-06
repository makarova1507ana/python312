"""
Написать регулярное выражение для определения валидных логинов.
# Валидными считаются те логины, которые удовлетворяют следующим условиям:
# ● содержится минимум 1 букву латинского алфавита и не содержится буквы других алфавитов
# ● содержит минимум 2 цифры
# ● в конце имени обязательно нужно указывать “login”
# примеры валидных значений
#   n12login
#   name22login
#   2name2login
# и т.д.
\w{3,}login$
namelogin
name1login

"""
import re

# import re
# #logins = ["nlogin", "n12login"]
# login = "n12login"
# is_valid_login = len(re.findall("\w{3,}login$", login)) # 1 - валидный,  0 - невалидный
# print(is_valid_login)
# digits = re.findall("\d", login)
# alphas = re.findall("[A-z]", login)
# print(len(digits))
# print(alphas) #login - 5 букв + 1 и больше
# # 1 Опеределяем прибилизительность валидности -> \w{3,}login
# #       2 Если 1 пункт успешный, то выполянем подсчет кол-во букв и цифр
# #           2.1 считаем кол-во букв по такому шаблону "[A-z]"
# #           2.2 считаем кол-во цифр по такому шаблону "\d"





# --------------  Практика --------------- #
#
# #—------------------------------- Задача —--------------------------------#
# # Дана строка вида 00,00 или 00.00
# # Если дана 00,00, то необходимо провести замену “,”
# # на “.”. После выполнить преобразование к типу float
#
# s = '12.30'
# s = s.replace(',', '.')
# s = float(s)
# print(s)


# #—------------------------------- Задача —--------------------------------#
# # Дана строка вида https://site.com/catalog/"имя"
# # необходимо показать надпись "адрес существует", если "имя" содержит только буквы Русской Кириллицы
# # https://site.com/catalog/{содержатся только буквы Русского алфавита}
# # https://site.com/catalog/абвгд - валидный
# # https://site.com/catalog/75489 - невалидный
#
# url = r"https://site.com/catalog/абвгд"
# re_exp = r"https:\/\/site\.com\/catalog\/[А-Яа-я]+$"
# is_url = len(re.findall(re_exp, url)) # 1 - валилный,  0 - невалидный
# print(is_url)


# #—------------------------------- Задача —--------------------------------#
# #  проверить валидность ссылки
# import re
# regex = re.compile(
#         r'^(?:http|ftp)s?://'
#         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
#         r'localhost|'
#         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
#         r'(?::\d+)?'
#         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
#
# print(re.match(regex, "http://site.com/catalog/животные") is not None)
# print(re.match(regex, "site.com") is not None)




# #—------------------------------- Задача —--------------------------------#
# # найти имя файла с расширением .txt в строке
#
# test = '''
# file.txtT
# file1.txt
# file.png
# file.jpg
# %%fd.txt
# '''
#
# reg_exp = r'\n\w{1,}\.txt[\n$]'
# print(re.findall(reg_exp, test))






# #—------------------------------- Задача —--------------------------------#
# # посчитать кол-во слов в тексте. Слово считаете последовательность только из букв английского или русского алфавита
# # разделителем слов может служить [пробел, ",", "." ":", "!", "?", ";"]
# text = "hello Котик! Это я твой friend. Сегодня мы будем веселиться, петь, dance."
# re_exp = r"[A-zА-я]+[, .!?]"
# words = re.findall(re_exp, text)
# print(len(words))
#
#
# # еще один способ
# print(re.split(r"[, .!?]", text))
#
#
# # #  еще один способ
# # import string
# #
# # text = 'Hello Котик! Это я твой frriend. Сегодня мы будем веселиться, петь и танцевать.'
# #
# # text = text.translate(str.maketrans('', '', string.punctuation))
# # text = text.split()
# # print(len(text))







#
#
# # ------------------------- Функции ----------------------------------- #
# # функция - действие
# # print()
# # len()
# # max()
#
# # функция - сохраненный(именованый) набор действий выполняющий какую-то одну конкретную задачу
# #
# # def(define - объявить) function_name(parameters):
# #     action1
# #     ...
#
# # function_name() # вызов функции
#
# from turtle import *
# from time import sleep
#
# def draw_triangle(a): # a - параметр или аргумент  (в нашем случае длина стороны )
#     forward(a)
#     left(120)
#     forward(a)
#     left(120)
#     forward(a)
#     left(120)
#
#
# length_side_triangle = 200
# draw_triangle(length_side_triangle) #вызов функции
#
# left(60)
# draw_triangle(length_side_triangle)
#
# forward(length_side_triangle)
# right(120)
# draw_triangle(length_side_triangle)
#
#
# sleep(5)
#
#

# #—------------------------------- Задача —--------------------------------#
# # восьмиугольник.png
# #
# #
# from turtle import *
# from time import sleep
#
# def draw_octagon():
#     color("blue")
#     for side in range(8):
#         forward(100)
#         left(180-135)
#
#
# for i in range(8):
#     draw_octagon()
#     left(360/8)
#
# sleep(2)





# # # ------------------------Задача--------------------------#
# # написать функцию(a, b, c), проверяет существование треугольника
# # is_valid_triangle(a,b,c)
#
# def is_valid_triangle(a, b, c):
#     if a + b > c and c + b > a and a + c > b:
#         print("треугольник существует")
#     else:
#         print("треугольник не существует")
#
# is_valid_triangle(5, 3, 2)
# is_valid_triangle(5, 5, 5)



# ------------------------Задача--------------------------#
# написать функцию для нахождения кол-во букв в строке

def count_alpha(text_for_func):
    print(len(re.findall(r"[A-z]", text_for_func)))


count_alpha("Hello, kitty! 1234")