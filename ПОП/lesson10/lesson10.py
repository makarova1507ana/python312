#
# # —------------------------------- Задача —--------------------------------#
# # Напишите функцию для вычисления
# # перемитра произвольного n-угольника
#
# def check_sides(list_sides):
#     if len(list_sides) >= 3: # минимум 3 стороны
#         for side in list_sides:
#             if side <= 0:
#                 return False # side <=0
#         return True # Если все стороны в кортеже > 0
#     return False # Если len(list_sides) < 3:
#
# def P_n_angle(list_sides: tuple):
#     P = 0
#     if check_sides(list_sides):
#         for side in list_sides:
#             P += side
#     return P # P==0 - какие-то неверные значения
# # list_sides = (5, 5)
# # print(P_n_angle(list_sides))
#
#
#
#
# #------произвольное кол-во параметров в функции *sides-----#
# def P_n_angle(*sides): # *sides -  позволяет передавать произвольное кол-во аргументов
#     P = 0
#     if check_sides(sides):
#         for side in sides:
#             P += side
#     return P # P==0 - какие-то неверные значения
#
# #print(P_n_angle(5, 5, 5, 5))





# #------ произвольное кол-во именованных параметров в функции *sides-----#
# def check_sides(list_sides):
#     if len(list_sides) >= 3: # минимум 3 стороны
#         for key in list_sides:
#             if list_sides[key] <= 0:
#                 return False # side <=0
#         return True # Если все стороны в кортеже > 0
#     return False # Если len(list_sides) < 3:
# def P_n_angle(**sides): # **sides-> словарь -  позволяет передавать произвольное кол-во аргументов
#     P = 0
#     if check_sides(sides):
#         for key in sides:
#             P += sides[key]
#     return P # P==0 - какие-то неверные значения
#
# print(P_n_angle(a=5,b=5,c=5))


#—------------------------------- Задача —--------------------------------#
# Написать функцию по генерации пароля для пользователя.
# Требования: длина от 6 до 20 символов,
# должен быть ровно один символ подчеркивания,
# хотя бы две заглавных буквы, не более 5 цифр,


# Алгоритм
# Валидные пароли
# AbC_bbb
# Ab_C55
# ACD_AAA
# 0_0ABc

# невалидные пароли
# fddddd
# Ab_C_55
# 555555
# 0_0Abc
# fg5
# F_G
# aaaaaaaaaaaaaaaaaa_AA

import random
import re
def generate_string(count, string):
    result = ''
    for i in range(count):
        result += random.choice(string)
    return result

def is_valid_password(password):
    count_digits = len(re.findall(r'\d', password))
    count_symbol_ = password.count('_')
    count_alpha_upper = len(re.findall(r'[A-Z]', password))
    return len(password) >= 6 and len(password) <= 20 and count_digits <= 5 and count_symbol_ == 1 and count_alpha_upper >= 2

#print(is_valid_password(r'\dPArrr3333sseod_')) # для тестов

def generate_password(count_digits, count_symbol_, count_alpha_upper, count_alpha_lower):
    digits = "0123456789"
    symbol_ = "_"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    part1 = generate_string(count_alpha_upper, alpha)
    part2 = generate_string(count_symbol_, symbol_)
    part3 = generate_string(count_alpha_lower, alpha).lower()
    part4 = generate_string(count_digits, digits)
    password = part1 + part2 + part3 + part4
    if is_valid_password(password):
        return password
    return generate_password(count_digits=5, count_symbol_=1, count_alpha_upper=6, count_alpha_lower=1) # Рекурсия



#print(generate_password(count_digits=1, count_symbol_=1, count_alpha_upper=2, count_alpha_lower=2))






# -------------------------------функции высшего порядка -------------------------------------- #
# функции высшего порядка - это такие функции, которые принимают в качестве параметра другие функции
# import functools
# filter
# map
# reduce

#def is_positive(num): return num > 0 # == lambda num: num > 0

# # Лямбда функции - функция, у которой нет имени. Будет всегда иметь возвращаемое значение
# is_positive = lambda num: num > 0 # is_positive - почти обычная переменная
# print((lambda num: num > 0)(5))
# print(is_positive(5))
# is_positive = -5
# print(is_positive)


# filter(Что надо сделать (функцию), набор значений)

# # Дан список чисел, необходимо сформировать новый список чисел только с положительными значениями
# nums = [5, -4, 6, 8, -2, 0, 4]
# result = list(filter(lambda num: num > 0, nums))
#
# print(result)

# еще примеры
# print((lambda num1, num2: num1 > num2 ) (5, 4))
# print((lambda string: len(string) > 0 ) ('Hello', 4))
# print((lambda num: num**2)(5))


# map(Что надо сделать (функцию), набор значений) -> для преобразования текущего списка

# # Дан список чисел представленных в строковом формате, создать новый список в формате float
# string_nums = ['1', '2', '-50', '5.5']
# nums = list(map(lambda num: float(num), string_nums))
# print(nums)



# # Дан список значений представленных в строковом формате, создать новый список в формате float
# strings = ['1', '2', '-50', '5.5', '5,5', '55', '8943', '-4,32', '54-33', 'ghgh60']
#
# reg_exp = "-{0,1}\d+[.]{0,}\d?"
# nums = list(filter(lambda num: re.fullmatch(reg_exp, num), strings))
# nums = list(map(lambda num: float(num), nums))
# print(nums)


# import functools # function tools
#
# # reduce (Что надо сделать (функцию), набор значений) ->  если надо работаь с двумя значениями в лямбде функции
#
#
# # sum () попробуем реализовать ее аналог
#
# s = functools.reduce(lambda result, num: result + num, [5, 5, 5])
# print(s)









# # Дан список строковых значений. Найти самое длинное значение состоящее из букв.
# # Если таких значений несколько, то сформировать список со всеми сопадениями
# l = ["tree", "Zooo", "124,54", "zoo 123", "4234", "<989./", "хао"]
#
# # пример выводa
# # tree
# # Zooo
#
# # Алгоритм
# # 1. отфильтровать только буквенные строки
# l = list(filter(lambda string: string.isalpha(), l))
#
# # 2. найти самое длинное слово
# lengths = list(map(lambda string: len(string), l))
# max_length = max(lengths)
# l = list(filter(lambda string: len(string) == max_length, l))
# print(l)

import  functools
# дан список целых чисел (не нужно делать дополнительные проверки на тип данных)
# сформировать новый список четных значений и отдельно вывести их общее произведение
nums = [5, 67, 89, 44, 2]
nums = list(filter(lambda num: num % 2 == 0, nums))
print(nums)
res_multiplies = functools.reduce(lambda  result, num: result*num, nums)
print(res_multiplies)



















# ---------------------------------- ДЗ ---------------------------------------#
# разбить функцию на смысловые части и для этих частей написать новые функции
# исправить баги

import random
import string

def is_valid_password(password):
    count_digits = len(re.findall(r'\d', password))
    count_symbol_ = password.count('_')
    count_alpha_upper = len(re.findall(r'[A-Z]', password))
    return len(password) >= 6 and len(password) <= 20 and count_digits <= 5 and count_symbol_ == 1 and count_alpha_upper >= 2

def pass_gen():
    n = random.randint(6, 20)
    pos_underline = random.randint(0, n)
    pos_first_uppercase = random.randint(0, n)
    while pos_first_uppercase == pos_underline:
        pos_first_uppercase = random.randint(0, n)
    pos_second_uppercase = random.randint(0, n)
    while pos_second_uppercase == pos_underline or pos_second_uppercase == pos_first_uppercase:
        pos_second_uppercase = random.randint(0, n)
    prev_digit_idx = -2
    digits_counter = 0

    ans = ''
    for idx in range(n):
        if idx == pos_underline:
            ans += '_'
            continue
        if idx == pos_first_uppercase or idx == pos_underline:
            ans += random.choice(string.ascii_uppercase)
            continue
        char = random.choice(string.ascii_letters + string.digits)
        if char == '_':
            continue
        if char in string.digits:
            digits_counter += 1
            if digits_counter > 5 or prev_digit_idx == idx - 1:
                continue
            prev_digit_idx = idx
            ans += char
            continue
        ans += char
    return ans


# print(is_valid_password(pass_gen()), pass_gen())
