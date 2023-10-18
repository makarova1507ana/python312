# ------------------------------------------ Циклы ------------------------------------------------ #
# циклы - повторение чего-либо
# while - цикл с условием (до тех пор пока ПРАВДА)
# for - цикл перебора значений ( до тех пока не будет перебраны все элементы)



# # ------------------------------------------ while ------------------------------------------------ #
# # while Условие:
# #   action1
# #   ...
#
# n = 10 # кол-во грязных тарелок
# while n != 0:
#     print("Берем грязную тарелку")
#     print("Моем грязную тарелку")
#     n -= 1 # n = n - 1
#     print(f"осталось грязных тарелок = {n}")
#     print("Ставим чистую тарелку сушиться", end = '\n ------------------------------- \n')
#

# # # ------------------------ЗАДАЧА------------------------------#
# # # Квадрат при помощи черепахи
#
# from turtle import* # * - все что есть в turtle
# from time import sleep
#
# lines = 0
# while lines != 4:
#     forward(100)# вперед
#     left(90) #налево
#     sleep(1)
#     lines += 1
#
# sleep(5)

# -----------------------------операторы циклов------------------------------#
# break - прерывание цикла
# continue - переход к следущей итерации
# else - блок выхода из цикла (если не было прерываний)


# # ------------------------ЗАДАЧА------------------------------#
# # игра Угадай число.
# # Компьютер загадывает целое число (1 до 100).
# # Задача пользователя отгадать число
#   Если введет 0 - то выход из программы
# # Алгоритм
# # 1.Компьютер загадывает число.
# # Пользователь вводит свой ответ
# # Сравниваем число_пользователя == число_компьютера
#
# # сделаем рандомное число
#
# import random
# computer_number = random.randint(1, 3)
# runnig = True
# while runnig:
#     user_number = int(input(" your number: "))
#     if user_number != computer_number:
#         print("Не угадали!")
#         continue # код ниже в этой конструкции исполнен не будет
#     if user_number == computer_number:
#         print("Ура угадали число")
#         break # экстренное прерывание  - переход сразу на 70 строку
#     elif user_number == 0:
#         runnig = False
# else:
#     print("КОНЕЦ ИГРЫ \nВам так и не удалось отгадать число")
# print("КОНЕЦ ПРОГРАММЫ")


# # -----------------------------цикл for------------------------------#
# # перебор чего либо
# # for кэш in набор_значений:
# #   инструкции
#
# print("--------------------------------")
# for color in 'red', 'blue', 'black':
#     print(color)
#
# print("--------------------------------")
# for num in 1, 5, -1:
#     print(num)
#
# print("--------------------------------")
# for variable in 3, "smth string", 1.00:
#     print(variable)
#
# print("--------------------------------")
# for variable in "HEllo world!":
#     print(variable)


# # #-------------------- Задание --------------------#
# # # нужно напечатать с 5 до 5000
# number = 5000
# value = 5
#
# while number > value:
#     print(value)
#     value += 1



# # #-------------------- Задание --------------------#
# # # Нарисовать квадрат, у которого все 4 стороны разного цвета (свои цвета)
# # через for
#
# import turtle
# from time import sleep
# screen = turtle.Turtle()
#
# # Цвета на черчение
#
# for color in "red", "green", "blue", "purple":
#     screen.pencolor(color)
#     screen.forward(100)
#     screen.right(90)
#     sleep(2)
#
# turtle.done()
# sleep(5)



# ------------------------------- range - диапозон  ----------------------------------#
# start - включительно (ТОЛЬКО int)
# end - не включительно (ОБЯЗАТЕЛЬНЫЙ ПАРАМЕТР) ( ТОЛЬКО int)
# step - шаг (ТОЛЬКО int)
# range(start, end, step)

# print("--------------------------------")
# end = 5
# d = range(end) # start = 0 и step = 1 по умолчанию
# print(d)
# for element in d:
#     print(element)

# print("--------------------------------")
# end = 10
# start = 5
# d = range(start, end)#step = 1 по умолчанию
# print(d)
# for element in d:
#     print(element)



# print("--------------------------------")
# end = 20
# start = 5
# step = 3
# d = range(start, end)
# for element in d:
#     print(element, end=" ")
#
# d = range(start, end,  step)
# print('\n', d)
# for element in d:
#     print(element)



# print("--------------------------------")
# end = 20
# start = 5
# step = -1
# d = range(end, start,  step)
# print( d)
# for element in d:
#     print(element)



# # ---------Если надо с float---------#
# # !!! работает криво !!!
# import numpy
# print("--------------------------------")
# end = 5
# start = 0.2
# step = 0.2
# d = numpy.arange(start, end, step )
# print(d)
# for element in d:
#     print(element)






# #----------------- Задание ------------------#
# # дано число (любое число)
# # показать столбик с умножением на это число от 2 до 9

#
#
# number = int(input('Введите число: '))
#
# for i in range(2, 10):
#     print(f'{i} * {number} = {i * number}')
#




# # #----------------- Задание ------------------#
# # spiral_square.png нарисовать как на картинке


# from turtle import*
# from time import*
# max_side = 500
# start_side = 10 # side - длина стороны
# d = 10 # на сколько надо увеличивать сторону
# for side in range(start_side, max_side, d*3):# d*3 (потому что 3 цвета)
#     for c in "red", "green", "blue":
#         color(c)
#         forward(side)
#         left(90)
#         side += d
#
# sleep(5)


# # #----------------- Задание ------------------#
# # turtle_result.jpg нарисовать как на картинке
# from turtle import*
# from time import*
#
# for i in range(1,5):
#     color('red')
#     circle(80)
#     left(30)
#     color('green')
#     circle(80)
#     left(30)
#     color('blue')
#     circle(80)
#     left(30)
#
# sleep(3)

#
# # --------------------- ЗАДАЧА -------------------------- #
# # """
# # Пользователь вводит с клавиатуры два числа(включительно). Нужно
# # посчитать сумму чисел в указанном диапазоне, а также
# # среднеарифметическое.
#
#
# start = 0
# end = 7
#
# total = 0
# count = 0
# if start > end:
#     start, end = end, start
#
# for number in range(start, end + 1):
#     total += number
#     count += 1
#
# if count != 0:
#     average = total / count
#
# print(f"Сумма чисел в диапазоне от {start} до {end} равна {total}")
# print(f"Среднее арифметическое равно {average}")








# # # ------------------------ЗАДАЧА------------------------------#
# нарисовать солнышко
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()














# ------------------------------ Коллекционный тип данных----------------------------------- #
# коллеция - набор значений  (массив)
# array - массив - надо подключать - динамеческий размер + одинаковый тип данных
# list - список
# tuple - кортеж
# set - множетсво
# dict (dictinary) - словарь
#

# import array
# arr = array.array('i', [1, 104, 45, 98])#
# arr.append('*')
# for el in arr:
#     print(el)

# list - динамический размер, но значения могут быть любого типа
# l = ['Heelo', 5, 5.54, [11,'3']]
# l[0] = 'H'  #l[0] - обращение по индексу

# tuple - кортеж
# значения могут быть любого типа
# Но нельзя изменить
# t = (1, "Hello", [2, 3])
# t[0] = 5 # TypeError: 'tuple' object does not support item assignment


# # # set - множетсво
# # # динамический размер
# # # хранит только уникальные значения
# l = ['0',8,1,1,1,1,2,111111,3,4,5,7,1, '1']
# s = set(l)
# print(s)

# dict (dictinary) - словарь
# динамический размер
# ключ(Должны быть уникальные): значение(может повторяться)
d = {"key": 1, 2: "2"}