
# #—------------------------------- Задача —--------------------------------#
# #дан файл, в каждой строке, которого содержатся имя товара и его тип через запятую
# # (одежда, еда, канцелярия, тип может быть не указан вовсе,
# # в таком случае стоит создать файл “другое.txt”).
# #создать  файл одежда.txt и записать в него все наименования одежды и т.д.
#
# # 1. Прочитать файл и разбить товары по категориям
#
#
#
# # 1. Прочитать файл и разбить товары по категориям
# with open("products.txt", "r", encoding="utf-8") as f:
#     products = f.readlines()
# print(products) # -> {'одежда': ['Футболка', 'Джинсы' ...], 'еда': ['Молоко', 'Хлеб' ...]}
# types = {}
# for product in products: # product = 'Футболка, одежда\n' ...
#     product = product.replace('\n', '')
#     product = product.replace(' ', '')
#     type_product = product[product.find(',')+1:]
#     name = product[:product.find(',')]
#     if type_product == '':
#         type_product = 'другое'
#
#     #print([type_product])
#
#     if not(type_product in types.keys()):
#
#         types[type_product] = [name] # 'одежда': ['Пальто']
#     else:
#         types[type_product].append(name) # types[type_product] -> ['Пальто']
# print(types)
#
# # 2. категории записать в соответствующие файлы
# for key in types:
#     with open(key+'.txt', 'w', encoding='utf-8') as f:
#         text = '\n'.join(types[key]) # types[key] - > ['Молоко', 'Хлеб', 'Сок', 'Яблоко', 'Банан'],
#         # text -> 'Молоко\nХлеб\n...'
#         f.write(text)



