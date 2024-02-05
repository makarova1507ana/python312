# 140 питон
# последние 2 пары экзамен 03.07
# 3-4 недели к дп

# Паттерны проектирования - теория
# Асинхронное программирование - теория

# тестирование (модульные тесты)
# логирование

# -------------------------------- тестирование ----------------------------------------#
# тестирование - процесс определяющий соответствие между ожидаемым и
# реальным поведением программы(или компонента)
# passed - пройден тест успешно (ожидаемое поведение == фактическому поведению)
# failed - пройден тест не успешно (ожидаемое поведение != фактическому поведению)
# skipped - тест пропущен ()

# цель тестирования - (ожидаемое поведение == фактическому поведению),
# бонусом выявить потенциальных несоответствий

# 1. "тест-кейсы" - мы будем описывать ожидаемое поведение программы
# 2. написание модульных тест
# 3. Анализ результатов

'''
Проверка существования треугольника
@param [in] a - сторона треугольника
@param [in] b - сторона треугольника
@param [in] c - сторона треугольника
@return bool - True, если треугольник существует, и False в противном случае
'''
def is_triangle(a: [float, int], b: [float, int], c: [float, int]) -> bool:
    return a + b > c and a + c > b and c + b > a
# как должно быть? :
#  сумма длин любых двух сторон треугольника должна быть больше длины третьей стороны,
#  а разность длин любых двух сторон должна быть меньше длины третьей стороны.

# базовый тест (sanity test / smoke test):
# Передача "НОРМАЛЬНЫХ" входных параметров и получение ожидаемого результат
# ---- test case 1 ------# - обязательно базовым
# expected result: is_triangle(5, 5, 5) -> True
# actual result:
# ---- test case 2 ------#
# expected result: is_triangle(1, 2, 4) -> False
# actual result:
# ---- test case 3 ------#
# expected result: is_triangle(-5, -5, -5) -> False
# actual result:
# ...



#----------------------------------------------------#
# ---- test case 1 ------# - обязательно базовым
# expected result: is_triangle(5, 5, 5) -> True
# actual result:  is_triangle(5, 5, 5) -> True
a = 5
b = 5
c = 5
print(f"a={a}, b{b}, c={c}, is_triangle({a},{b},{c}) -> {is_triangle(a,b,c)}")

# --------- result - > test passed----------------#



# ---- test case 2 ------#
# expected result: is_triangle(1, 2, 4) -> False
# actual result:  is_triangle(1, 2, 4) ->False
a = 1
b = 2
c = 4
print(f"a={a}, b{b}, c={c}, is_triangle({a},{b},{c}) -> {is_triangle(a,b,c)}")

# --------- result - >  test passed ----------------#

# ---- test case 3 ------#
# expected result: is_triangle(-5, -5, -5) -> False
# actual result:  is_triangle(-5, -5, -5) ->
a = -5
b = -5
c = -5
print(f"a={a}, b{b}, c={c}, is_triangle({a},{b},{c}) -> {is_triangle(a,b,c)}")

# --------- result - >  test passed ----------------#


import random
import string
'''
требования к паролю, описанные в функции generate_secure_password, включают в себя следующие:
 * Длина пароля: Пароль должен иметь длину не менее 8 символов.
 * Все символы из ASCII: Все символы пароля должны соответствовать ascii
 * Минимум одна цифра: Пароль должен содержать как минимум одну цифру.
 * Минимум одна заглавная буква: Пароль должен содержать как минимум одну заглавную латинскую букву.
'''

'''
Генерация безопасного пароля с заданными требованиями
@param [in] length - длина пароля (минимум 8 символов)
@return str - безопасный пароль
'''
def generate_secure_password(length: int) -> str:
    if length < 8:
        raise ValueError("Длина пароля должна быть не менее 8 символов")

    # Генерация пароля, удовлетворяющего требованиям
    while True:
        password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
        if any(c.isdigit() for c in password) and any(c.isupper() for c in password):
            return password

# Эквивалентное тестирование
# определяем валидные значение : Qw123456
# Qw123456/

# определяем невалидные значения: парольвосемь

# Тестирование граничных значений
# qw123456 -нет заглавной буквы
# Qw12345 - длина меньше 8
# qweeerrr - нет цифры
# Йw123456 - используется не латиница

# ------------- test case ----------#
# expected result: generate_secure_password(8)
# ожидаю получить пароль подобного типа:
# Qw123456
# length: 8+
# digits: True # any  (хотя бы 1 Правда и более в перебираемой коллекции)
# Latin case: True # all  (все символы соответствовали таблицы ascii)
# Upper case:True (хотя бы 1 и более)
length = 8
actual_password = generate_secure_password(length)
print(f"""generate_secure_password({length}) -> {actual_password} 
length: {len(actual_password)} 
digits: {any(c.isdigit() for c in actual_password) }
Latin case: {all(c.isascii() for c in actual_password)}
Upper case: {any(c.isupper() for c in actual_password)}""")




# ------------- test case 2 ----------#
# expected result: generate_secure_password(3)
# ожидаю получить ValueError
length = 3
try:
    actual_password = generate_secure_password(length)
except ValueError:
    print("get exeption ValueError")


# #---------------аналог any-----------------------#
# count_is_digit = 0
# for c in actual_password:
#     if c.isdigit():
#         count_is_digit += 1

# # #---------------аналог all-----------------------#
# count_is_ascii = len(actual_password)
# for c in actual_password:
#     if not(c.isascii()):
#         count_is_ascii = 0
#         break
# if count_is_ascii != len(actual_password):
#     result = "password is not ascii"









'''
Проверка, является ли год високосным
@param [in] year - год для проверки
@return bool - True, если год високосный, и False в противном случае
'''
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


'''
Проверка, является ли год високосным
@param [in] year - год для проверки
@return bool - True, если год високосный, и False в противном случае
'''
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#Эквивалентное тестирование
# определяем валидные значения:
#  * високосный год: 2116 2012 2016 2020 2024
print(is_leap_year(1764))
#  * не високосный год: 2013, 2014,2015
print(is_leap_year(2013))


# невалидные значения: ddfd vfdv xcvc
#print(is_leap_year("ddfd"))

#test case 1: -> passed
# expected result: is_leap_year(2024) - True
# actual result: is_leap_year(2024) - True
print(is_leap_year(2024))

#test case 2: -> passed
# expected result: is_leap_year(2024.1) - False
# actual result: is_leap_year(2024.1) - False
print(is_leap_year(2024.1))

#test case 3: -> failed
# expected result: is_leap_year(-2024) - False
# actual result: is_leap_year(-2024) - True
print(is_leap_year(-2024))






# # ---------------------------модульные тесты-------------------------------------- #
# # это спецаильные функции, которые тестируют ваш модуль, чаще всего описывают тест кейсы
# import pytest
#
# def test_is_leap():
#     # expected result: True
#     # actual result: is_leap_year(2024)
#     expected_result = True
#     actual_result = is_leap_year(2024)
#     assert expected_result == actual_result