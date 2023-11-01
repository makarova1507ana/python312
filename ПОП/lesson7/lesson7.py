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


#l = ['apple', 'apple', 'banana', 'banana', 'kiwi', 'avokado', 'apple']
# for el in l:
#     print(el)
#
# for i in range(len(l)):
#     print(l[i])

# --------объединение ---------#
# example for test program
#l = ['apple', 'apple,', 'banana', 'banana', 'kiwi', 'avokado', 'apple']


l = s.split(' ')
print(l)
for i, el in enumerate(l):
    print(i, el)
    if i != len(l)-1 and el.isalpha() and l[i+1].isalpha():
        if el == l[i+1]:
            l.remove(el)
    else:
        if i != len(l)-1:
            is_word_for_remove = True
            for j in range(min(len(el), len(l[i+1]))):
                if el[j] != l[i+1][j]:
                    is_word_for_remove = False
                    break
            if is_word_for_remove:
                if len(el) < len(l[i + 1]):
                    word_for_remove = el
                else:
                    word_for_remove = l[i+1]
                l.remove(word_for_remove)

result = ' '.join(l)
print(result)