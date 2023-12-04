# # Дан массив. Найдите два соседних элемента,
# # сумма которых минимальна.
# # arr = [1, 1, -2, 3, 0, 5]
# # # 1 1 = 2
# # # 1 -2 = -1
# # # -2 3 = 1
# # # 3 0 = 3
# # # 0 5 = 5
# # min_sum = 10**1000
# #
# # for i in range(len(arr)-1):
# #     sum_neighbours = arr[i] + arr[i+1]
# #     if min_sum > sum_neighbours:
# #         min_sum = sum_neighbours
# #         neighbours_min_sum = [arr[i], arr[i+1]]
# #
# # print(neighbours_min_sum)
#
#
# import functools
#
# # -----------------------2 ---------------
# arr = [-10, 1, -2, 3, 0, -5,1,1]
# # -10 1 = -9
# # 1 -2 = -1
# # -2 3 = 1
# # 3 0 = 3
# # 0 -5 = -5
# # ...
# indexies = range(len(arr)-1)
# # найди суммы всех соседних элементов
# res = list(map(lambda index: arr[index]+arr[index+1], indexies))
# #print(res)
#
#
# # найти минимальный элемент и его индекс
# index_of_min_sum = res.index(min(res))
# #print(index_of_min_sum, min(res))
#
# # по идексу мин. эл. ищем его пары чисел в изначальном списке
# # по формулу arr[index], arr[index+1]
# res = (arr[index_of_min_sum], arr[index_of_min_sum+1])
# #print(res)
#
#

# ---------------------- Работа с файлами -------------------------------- #
# Задачи по работе с файлами
# 1. Научиться работать с ОС
# 2. Действия с файлами (создание, чтение, редактирование и удаление)

# #—------------------------------- Задача —--------------------------------#
# # дан файл, в каждой строке которого содержится стоимость товара.
# # Найти самый дорогой товар, самый дешевый товар и
# # общую сумму покупки.
# # открыть и извлечь все строки из файла -> ['5', '545', ...]
# # ['5', '545', ...] -> [5, 545, ...]
# # max([5, 545, ...]), min([5, 545, ...]), sum ([5, 545, ...])
#
# with open("prices_of_products.txt", "r") as f:
#     prices = f.readlines()
# print(prices)
# prices = list(map(lambda el: float(el), prices)) # -> [100.0, 500.0, ... ]
# print(prices,
#       "\n",
#       f"max = {max(prices)}",
#       f"min = {min(prices)}",
#       f"sum = {sum(prices)}")

# #test = int(" 54545 \n")
# test = int(" 54545 \n")
# print([" 54545 \t"])
# print(type(test))





##—------------------------------- Задача —--------------------------------#
# дан файл, в каждой строке которого содержится фамилия человека.
# Найти всех людей фамилия, которых начинается на К (rus)
# ["family1", ...]
# for family in ["family1", ...]
#   family[0] == "К" или "к"
#
# with open('second_names.txt', 'r', encoding='utf-8') as f:
#     last_names = f.readlines()
#
# print(last_names)
#
# valid_lnames = []
#
# for name in last_names:
#     if name[0] == 'К' or name[0] == 'к':
#         valid_lnames.append(name)
#
# print(valid_lnames)



#-----------------------------------------2 -------------------------------
#
# lst = []
# lst_new = []
#
# with open("second_names.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         line = line[0].upper() + line[1:]
#         if line[0] == 'К':
#             lst_new.append(line.replace('\n', ''))
#
#
# print(lst_new)



# # -----------------------------3-------------------------------------#
# with open('second_names.txt', 'r', encoding='utf-8') as f:
#     last_names = f.readlines()
#
# print(last_names)
#
# valid_lnames = list(filter(lambda lname: lname[0].upper() == 'К', last_names))
#
#
# print(valid_lnames)


# -----------------------задача---------------------#
#  допустимый набор элементов (множества)
# дан файл, в котором произвольное кол-во строки, содержащие произвольные символы
# проверить удовлетворяет содержание файла допустимым символам
# допустимы только русские буквы, цифры, точка, запятая, \n, \t пробел и тире

# import re
# def is_valid_text(text):
#     return text == "".join(re.findall("[А-я .,\-ёЁ\n\t—]", text))
# with open("check_symbols.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#
# print(is_valid_text(text))



#------------------------------2------------------------------------------------#
# def is_valid_text(text):
#     ALLOWD_SYMBOLS = " АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя0123456789 ., -\n\t—"
#     return set(text) <= set(ALLOWD_SYMBOLS) #все символы текста (уникальные) text соотвествуют допустимым символам
# with open("check_symbols.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#
# print(is_valid_text(text))


#----------------------------------про множества ------------------------------#
# print(set("BA"), "<=", set("ABCD"), set("BA") <= set("ABCD"))
# print(set("BAR"), "<=", set("ABCD"), set("BAR") <= set("ABCD"))

# #----------------------------------пример птицами ------------------------------#
# birds = {"воробей", "ласточка", "аист"}
# migratory_birds = {"ласточка", "аист"}
# user_words = {"неворобей", "неголубь"}
# if user_words <= birds: #слова пользователя входят в состав множества птиц?
#     print(f"{user_words} это птица или птицы")
#     if user_words <= migratory_birds:
#         print(f"{user_words} это перелетная птица или перелетные птицы")
# else:
#     print(f"{user_words} это НЕ птица или птицы")


#-----------------------задача---------------------#
# 3,0 -> 3.0
# дан файл, в котором произвольное кол-во строки, содержащие произвольные символы
# отобрать только значения, которые можно преобразовать к числовым форматам,
# причем дробные значения, записанные через запятую ( пример 3,0)
# преобразовать в значения через точку (пример 3.0)
# целые числа записать в файл integers.txt
# дробные числа записать в файл float.txt
# (\-|)\d+(\.|,|)\d{0,} -общий шаблон
# ?? -шаблон для целых чисел
#  \d+[\.|,]\d+     шаблон для дробных  чисел
import re
def get_float_nums(text):
    return re.findall("\d+[\.|,]\d+", text)

with open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()

float_nums = list(map(lambda num: num.replace(",", "."), get_float_nums(text)))
print(float_nums)

with open("float.txt", "w") as f:
    f.write("\n".join(float_nums))






# -----------------------задача---------------------#
#  про животных и птиц