# # —------------------------------- Задача —--------------------------------#
# # Существует функция s_triangle(a, b), которая
# # находит площадь прямоугольного треугольника по двум
# # заданным катетам.
#
# # Требуется ли делать проверку, что треугольник прямоугольный ?
# # - нет, не требуется
# # Требуется ли проверка валидности сторон? - да, требуется.
# # Как находится площадь прям. треугольника ? - s = a * b * 0.5 (s = a * b / 2)
#
#
# def s_triangle(a: float, b: float):
#     #  а какие катеты могут быть(по типу данных)? - только числовые значения int или float
#     if a > 0 and b > 0:
#         return (a * b) / 2# формула не такая? (a * b) // 2
#         # где return ?
#
#     return 0 # формат обработки ошибки
#
#
# print("Площадь треугольника: ", s_triangle(2, 1))


# #—------------------------------- Задача —--------------------------------#
# #Существует функция conversion(start, end, value), которая переводит
# # из заданной единицы (мм, см, м, км) в (мм, см, м, км)
#
# # пример работы
# # conversion('мм', 'см', 100)
# # output: 100/10 = 10 # passed +
#
# # какие значение позволять провести качественное тестирование?
# # conversion('ммm', 'см', 100)
# # output: 0? # failed -
#
# # conversion('мм', 'см', -100)
# # output: invalid value # failed -
#
# # conversion('мм', 'мм', 100)
# # output: 100 # passed +
#
# # какие требования должна выполнять данная функция?
# #   перевод значения из заданной единицы измерения в указанную единицу
# #   валидность значений (числа(int || float) > 0, start и end  что-то из этого мм, см, м, км)
#
#
# # def conversion(start, end, value):
# #        d = {'мм': 1, 'см': 2, 'м': 3, 'км': 4}
# #        if d[start] > d[end]:
# #             return value * (10 ** d[end]) #здесь баг -
# #        elif d[start] < d[end]:
# #             return value // (10 ** d[start])
# #        else:
# #             return value
#
# # 'км' - 10**3
# # 'м' - 10**0
# # 'см' - 10**-2
# # 'мм' - 10**-3
#
# def conversion(start, end, value):
#     d = {'мм': -3, 'см': -2, 'дц': -1, 'м': 0, 'км': 3}
#     if start in d and end in d and value > 0: # проверяем valid?
#         if d[start] < d[end]:
#             return value / (10 ** (d[end] - d[start]))
#         elif d[start] > d[end]:
#             return value * (10 ** (d[start] - d[end]))
#         else:
#             return value
#     return -1# это ошибка неверного ключа
#
# # print(conversion('мм', 'см', 100)) # 10
# # print(conversion('мм', 'м', 1000)) # 1
# # print(conversion('мм', 'м', 100)) # 0.1
# # print(conversion('мм', 'км', 1000000)) # 1
# #
# # print(conversion('см', 'мм', 1)) # result = 10, but result =  10000
# # print(conversion('м', 'мм', 1)) # result = 1000, but result = 100
#
# #
# # print(conversion('смvv', 'мм', 100)) # keyError
# # print(conversion('см', 'мм', -100)) # invalid value






# #—------------------------------- Задача —--------------------------------#
# # Дана произвольная строка.
# # Подсчитайте в ней количество буквенных символов в любом регистре( то есть отдельно маленькие и большие) и
# # выведите результат на экран.
#
# import re
# def count_letter(string, register = 'lower'):
#     if register == 'lower':
#         lower_case = "[a-z]"
#         return len(re.findall(lower_case, string))
#     elif register == 'upper':
#         upper_case = "[A-Z]"
#         return len(re.findall(upper_case, string))
#
# test_string = "Hello Kitty!"
# count_upper_case = count_letter(test_string, 'upper')
# count_lower_case = count_letter(test_string, 'lower')
#
# print(f"lower_case = {count_lower_case}\nupper_case = {count_upper_case}")






# #—------------------------------- Задача —--------------------------------#
# # Дано строковое представление времени таймера '03:25:57'.
# # # Выведите на экран количество секунд, оставшихся до момента срабатывания таймера.
# # # Используйте формат сообщения «До срабатывания таймера осталось {n} сек.».
# # "00:01:33"
# # «До срабатывания таймера осталось 93 сек.».
# # часы >= 00
# # минуты < 60 and >= 00, если минут оказалось 60 и больше то увеличить часы на необходимо
# # секунды < 60 and >= 00, если минут оказалось 60 и больше то увеличить часы на необходимо
#
# def valid_time(time):
#     try:
#         hours = int(time[:2])
#         minutes = int(time[3:5])
#         seconds = int(time[6:])
#         if hours >= 0 and minutes >= 0 and seconds >= 0:
#             if seconds > 59:
#                 minutes += seconds // 60
#                 seconds = seconds % 60
#
#             if minutes > 59:
#                 hours += minutes // 60
#                 minutes = minutes % 60
#             return (hours, minutes, seconds)
#     except:
#         return (0, 0, 0)
#
#
# def sum_sec(time):
#     hours, minutes, seconds = valid_time(time)
#     hours = hours * 3600
#     minutes = minutes * 60
#     seconds = seconds
#     return f"До срабатывания таймера осталось {hours + minutes + seconds} сек"
#
#
# time = '03:25:61'
#
# print(sum_sec(time))
#
#


#—------------------------------- Задача —--------------------------------#
# Дана произвольная строка. Для корректной работы комментарий может быть отображен
# длинной не более 50 символов. Но с такой обрезкой появляется много казусов,
# например слова обрезаются не самым удачным образом.
# Составьте такое решение, где комментарий будет обрезаться с учетом длины <50 и
# без обрезанных слов.


# len(s) > 50
# до кого символа надо обрезать ?
#   как найти индекс первой буквы последнего слова?
import re
#------------ДЗ ------------------#
s = "Hello, Kitty! Cat is not a dog" # слова будем делить на основание пробелов
#len(s) - s[::-1].find(' ') - 1 # ищем индекс последнего пробела

if len(s) > 10:

    s = s[:10] # Hello, Kit
    #  найти ближайший(в меньше) по котором делать обрезку
    space_index = s.find(' ') #нашли пробел
    print(s[:space_index]) # Hello,
else:
    print(s)



#-----------2 способ ------------------#
#
# s = ""#
# list_s = s.split()
#
# result = []
#
# for i in range(len(list_s)):
#     if len(' '.join(result)) + len(list_s[i]) > 50:
#         break
#     else:
#         result.append(list_s[i])
#
# result = ' '.join(result)
# print(result, len(result))