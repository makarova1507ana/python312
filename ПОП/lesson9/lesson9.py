#----------------- Функции ----------------------#
# return  - возвращаемое значение
# параметры по умолчанию и аннотация

#—----------------- Задача -----------------------#
# Реализовать функцию для перевода из метров (m) в километры(km)
# и наоборот

# #—----------------- Логическая Задача -----------------------#
#
# # f1(n) - не имеет смысла
# def f1(n):
#     counter = 0
#     for i in range(10000):
#         for j in range(100000):
#             counter += 1
#             print(counter)
#             if n == 5:
#                 break
# f1(5) # 1 вопрос - сколько раз сработет print ?
# # 2 вопрос - почему именно столько раз?
#
# # f2(n) - не имеет смысла
# def f2(n):
#     counter = 0
#     for i in range(10000):
#         for j in range(100000):
#             counter += 1
#             print(counter)
#             if n == 5:
#                 return counter
# f2(5) # 1 вопрос - сколько раз сработет print ?
# # 2 вопрос - почему именно столько раз?
# #—----------------- Логическая Задача -----------------------#




# параметры функции?
# def conversion_length(length: float, unit: str = "m"): # unit="m" - параметр по умолчанию
#     if unit == "m":
#         return float(length * 1000) # return - вернуть результат вычисления
#     elif unit == "km":
#         return length / 1000 # return - точка выхода из функции
#
#     return 0 # что-то пошло не так
#     # Или вот так raise "Smth wrong"
#
#     #результат работы? return  -> float

# max_value = max([5, 3, 5, 4])
# print(max_value)
#
# console_print = print("Hello")
# print(console_print) # None - ? ничего


# print(conversion_length(5))
# print(conversion_length(5000, "km"))
#
# result = conversion_length(5000, "km")
# print(result)
#
# result = conversion_length(5)
# print(result)
#
# result = conversion_length(5, "kmmm")
# print(result)




#
# #—------------------------------- Задача —--------------------------------#
# # напиши функцию, которая будет рисовать квадрат
# # params:
# # is_fill - нужно ли делать заливку
# # a - длина стороны
# # color - цвет контура и заливки
# # нужен return _?_
# from turtle import *
# from time import sleep
#
# """
# @param a - length of a square
# @param is_fill - нужно ли закрашивать?
# @param col - color of square
#
# """
# def draw_square(a: int, is_fill: bool, col: str):
#     color(col)
#     if is_fill:
#         begin_fill()
#     for i in range(4):
#         forward(a)
#         left(90)
#     end_fill()
#
#
#
# draw_square(200, True, 'red')
# sleep(3)


# # —------------------------------- Задача —--------------------------------#
# # Напишите функцию для вычисления площади ромба
# # S_rombus(d1, d2) -> float S
#
# def check_values(d1, d2):
#     return d1 > 0 and d2 > 0
#     # вместо
#     # if d1 > 0 and d2 > 0:
#     #     return True
#     # return False
# def S_rombus(d1, d2): # Что делает? - вычисляет площадь ромба
#     if check_values(d1, d2):
#         return 0.5 * d1 * d2
#     return -1.0 # -1.0 - (или указание ошибку) невозможно вычислить значение
#
#
#
#
# print(S_rombus(-5, -4))

# —------------------------------- Задача —--------------------------------#
# Напишите функцию для вычисления
# перемитра произвольного правильного n-угольника

# def check_values(n, a):# n , a  локальная копия
#     return n >= 3 and a > 0
#
# def P_n_angle(n: int, a: int):
#     if check_values(n, a):
#         return n * a

# print(P_n_angle(10, 2))




# —------------------------------- Задача —--------------------------------#
# Напишите функцию для вычисления
# перемитра произвольного n-угольника

def check_sides(list_sides):
    if len(list_sides) >= 3: # минимум 3 стороны
        for side in list_sides:
            if side <= 0:
                return False # side <=0
        return True # Если все стороны в кортеже > 0
    return False # Если len(list_sides) < 3:

def P_n_angle(list_sides: tuple):
    P = 0
    if check_sides(list_sides):
        for side in list_sides:
            P += side
    return P # P==0 - какие-то неверные значения
list_sides = (5, 5)
print(P_n_angle(list_sides))




#------НАЧАТЬ С ЭТОГО *sides-----#
def P_n_angle(*sides):
    P = 0
    if check_sides(sides):
        for side in sides:
            P += side
    return P # P==0 - какие-то неверные значения
list_sides = (5, 5)
print(P_n_angle(list_sides))