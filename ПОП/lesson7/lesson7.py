#—------------------------------- Задача —--------------------------------#
# Необходимо исправить каждый повтор
# (слово, один или несколько пробельных символов,
# и снова то же слово).

# Ввод
# Довольно распространённая ошибка ошибка —
# это лишний повтор повтор слова слова.
# Смешно, не не правда ли? Не нужно портить хор хоровод.

# Вывод
# Довольно распространённая ошибка — это лишний повтор слова. Смешно, не правда ли? Не нужно портить хор хоровод.

s = """Довольно распространённая ошибка ошибка - 
это лишний повтор повтор слова слова. 
Смешно, не не правда ли? Не нужно портить хор хоровод.

"""
# print("хор" in "хоровод")

#l = ['apple', 'apple', 'banana', 'banana', 'kiwi', 'avokado', 'apple']
# for el in l:
#     print(el)
#
# for i in range(len(l)):
#     print(l[i])

# --------объединение ---------#
# example for test program
#l = ['apple', 'apple,', 'banana', 'banana', 'kiwi', 'avokado', 'apple']

#
# l = s.split(' ')
# print(l)
# for i, el in enumerate(l):
#     print(i, el)
#     if i != len(l)-1 and el.isalpha() and l[i+1].isalpha():
#         if el == l[i+1]:
#             l.remove(el)
#     else:
#         if i != len(l)-1 and abs(len(el) - len(l[i+1])) <= 2:
#             is_word_for_remove = True
#             for j in range(min(len(el), len(l[i+1]))):
#                 if el[j] != l[i+1][j]:
#                     is_word_for_remove = False
#                     break
#             if is_word_for_remove:
#                 if len(el) < len(l[i + 1]):
#                     word_for_remove = el
#                 else:
#                     word_for_remove = l[i+1]
#                 l.remove(word_for_remove)
#
# result = ' '.join(l)
# print(result)

#---------------------Регулярные выражения------------------------#

# test_string = """
# 0000 - не валидный
# 0011- не валидный
# 01- не валидный
# 0 - не валидный
#
# Валидные года:
# 9999
# 1234
# 586
# 20
# 1
# 2020
# """
# import re
# reg_exp = "[^0-9][1-9]\d{0,3}"
# result = re.findall(reg_exp, test_string)
# for i, string in enumerate(result):
#     result[i] = string.replace('\n', '')
# print(result)




#-------------задача----------------#
import re
# Дана строка номера телефона
# +7 999 999 99 99
# 8 999 999 99 99
test = ("""+7 999 999 99 99""")
reg_exp = r"((\+7|8) \d{3} \d{3} \d{2} \d{2})"
print(re.search(reg_exp, test).groups())
print(re.fullmatch(reg_exp, test).group())

