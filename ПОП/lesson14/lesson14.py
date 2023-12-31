# --------------------------------- Задача --------------------------------------#
# Дана строка Посчитать кол-во различных цифр
# в строке и создать словарь с указанием их кол-ва
# "Hello 1234567801! This is cat!"
# output: {1: 2, 2: 1, 3: 1 ... 0: 1 }
import re

#
# # Алгоритм
# # // перебрать каждый элемент
# # // если новый, то записываем в словарь, иначе находим в словаре
# # и прибавляем единицу
#
# s = 'Hellow3498576376713845321501dkfgnpudjkg'
#
# num_count = {
#     '0': 0,
#     '1': 0,
#     '2': 0,
#     '3': 0,
#     '4': 0,
#     '5': 0,
#     '6': 0,
#     '7': 0,
#     '8': 0,
#     '9': 0
# }
#
# for i in s:
#     if i in num_count:
#         num_count[i] += 1
#
# print(num_count)
#
#



# --------------------------------- еще одно решение --------------------------------------#
# string = 'Hello, 012345670! This is cat.'
# dictt = {}
#
# for i in string:
#     if i.isdigit():
#         dictt[i] = string.count(i)
#
# print(dictt)

# --------------------------------- еще одно решение --------------------------------------#
#
# import re
# s = 'Hellow3498576376713845321501dkfgnpudjkg'
#
# reg_exp = '[0-9]'
#
# nums = re.findall(reg_exp, s)
#
# num_count = {}
# for i in nums:
#     if i not in num_count:
#         num_count[i] = 1
#     else:
#         num_count[i] += 1
#
# print(num_count)




# # #—------------------------------- Задача —--------------------------------#
# # Дан список строк такого формата:
# # ["Имя: Яблоки, рублей за кг: 25, всего кг: 30",
# # "Имя: Груши, рублей за кг: 50, всего кг: 100",
# # "Имя: Молоко, рублей за шт: 55, всего шт: 200",
# # ... ]
# #
# #
# # Сформировать словарь с товарами. Выведите на экран все товары, цена которых не превышает 100 рублей. Проверку на правильность формата строки делать не нужно
# #
# #
# # пример
# # {"Яблоки": 750,
# # "Груши": 5000,
# # ... }
#
# # output: все товары превышают итоговую стоимость  100 рбулей
#
#
#
# # Алгоритм
# #  1 этап анализ списка строк (цикл нужен) # 2 этап преобразование строки в словарь
# #       берем одну строку и узнаем:
# #           1 имя товара (это будет ключ словаря) ?
# #           2 итоговая стоимость ( это будет значение ключа, найти числа и перемножить)
#
#
#
# lines = ["Имя: Яблоки, рублей за кг: 25, всего кг: 30",
#         "Имя: Груши, рублей за кг: 50, всего кг: 100",
#         "Имя: Молоко, рублей за шт: 55, всего шт: 200"]
#
# data = {}
# for line in lines:
#     # 1 имя товара (это будет ключ словаря) ?
#         a = line.index(' ') #нашли первый пробел
#         b = line.index(',')#нашли первую запятую
#         product = line[a + 1:b] # между 1-ым пробелом и 1-ой запятой фрукт
#         # print(product)#отладочная печать
#
#     #  2 итоговая стоимость ( это будет значение ключа, найти числа и перемножить)
#         # как найти число ? -> \d+
#         # ТОЛЬКО ДЛЯ ЦЕЛЫХ чисел
#         d = re.findall(r"\d+", line)
#         cost = int(d[0]) * int(d[1])
#         # print(cost) #отладочная печать
#
#
#     #  формируем
#         data[product] = cost
#
# #print(data)
# flag = True
# # 3 этап анализ словаря
# for key in data:
#     if data[key] < 100:
#         print(f"{key}: {data[key]}")
#         flag = False
# if flag:
#     print("все товары превышают итоговую стоимость  100 рбулей")



#



#
#
# # --------------------------------- еще одно решение --------------------------------------#
#
# dictlist = [
#     "Имя: Яблоки, рублей за кг: 25, всего кг: 30",
#     "Имя: Груши, рублей за кг: 50, всего кг: 100",
#     "Имя: Молоко, рублей за шт: 55, всего шт: 200"
# ]
#
# coast = {}
#
# for item in dictlist:
#     parts = item.split(', ')
#     name = parts[0].split(': ')[1]
#     price = int(parts[1].split(': ')[1])
#     quant = int(parts[2].split(": ")[1])
#
#     coast[name] = {'цена за единицу': price, 'количество': quant}
#
# # print(coast)
# for product_name, product_info in coast.items():
#     if product_info["цена за единицу"] <= 100 and product_info["количество"] >= 10:
#         print(f"Товар: {product_name}, Цена за единицу: {product_info['цена за единицу']} руб., Остаток: {product_info['количество']} кг")
#





#функция для формирования словаря  def make_dict(s) -> {"item": {'цена за единицу': price, 'количество': quant}}
def make_dict(s):
    parts = s.split(', ')
    name = parts[0].split(': ')[1] # нужна отдельная функция для поиска названиявания товара
    price = int(parts[1].split(': ')[1]) # нужна отдельная функция
    quant = int(parts[2].split(": ")[1])# нужна отдельная функция

    return name, {'price': price, 'count': quant} # return (element1, element2)


def filter_costs(data, cost):
    flag = True
    res = []
    for key in data:
        if data[key]['price'] * data[key]['count'] < cost:
            res.append(f"{key}: {data[key]}")
            flag = False
    if flag:
        return ("все товары превышают итоговую стоимость  100 рбулей")
    return res



lines = ["Имя: Яблоки, рублей за кг: 25, всего кг: 30",
        "Имя: Груши, рублей за кг: 50, всего кг: 100",
        "Имя: Молоко, рублей за шт: 55, всего шт: 200"]

result = {}
for line in lines:
    key, value = make_dict(line)
    result[key] = value

print(filter_costs(result, 1000))
