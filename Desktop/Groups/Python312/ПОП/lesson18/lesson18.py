#
# #-----------------------Создание JSON формата--------------------------#
# import json
# product = {"name": "apples 1 kg", "cost": 50}
# with open("product.json", "w") as f: # "w" - режим запись в файл
#     #json.dump(словарь, куда записываем, indent=кол-во пробелов перед ключом, sort_keys=True)
#     json.dump(product, f, indent=10)# f.write(json.dumps(product))
#     # удобнее читать человеку
#
#
#
# with open("product_dumps.json", "w") as f:
#     f.write(json.dumps(product))
# #-----------------------прочитать JSON формата--------------------------#
# # with open("player.json") as f:
# #     #print(f.read()) # обычная строка
# #     data = json.load(f)
# # print(type(data), data)
#
#
# with open("product.json") as f:
#     #print(f.read()) # обычная строка
#     data = json.load(f)
# print(type(data), data)
#


# # ---------------------------Практика----------------------------- #
# #
# # Создайте JSON файл для клиента, содержащий следующие поля: имя, фамилия, адрес электронной почты и возраст. Пример:
# #
# # {
# #   "имя": "Иван",
# #   "фамилия": "Иванов",
# #   "email": "ivan@example.com",
# #   "возраст": 30
# # }
# import json
# client = {
#     "имя": "Иван",
#     "фамилия": "Иванов",
#     "email": "ivan@example.com",
#     "возраст": 30,
#     }
#
# with open("client.json", "w", encoding="") as f:
#     json.dump(client, f, indent=2)



#—------------------------------- Задача —--------------------------------#
# дан JSON файл. Напиши CLI для получение информации о товаре.
# ПРИМЕР файла
#     {
#       "название": "Смартфон",
#       "цена": 500,
#       "категория": "Электроника"
#     }
# import json
# with open("product.json", encoding="utf-8") as f:
#     product = json.load(f)
# print(product)
# # ПРИМЕР
# # # CLI - command line interface
#
# name = product["название"]
# cost = product["цена"]
# category = product["категория"]
# while True:
#     command = input("""
# 1. покажи "название"
# 2. покажи "стоимость"
# 3. покажи "категория"
# """)
#     if command == "1":
#         print("название товара:", name)
#     elif command == "2":
#         print("стоимость товара:", cost)
#     elif command == "3":
#         print("категория товара:", category)
#     else:
#         break



# # ------------------------------- 2 ----------------------
# while True:
#     try:
#         command = input("""
# # 1. напиши "название"
# # 2. напиши "цена"
# # 3. напиши "категория"
# # 4. напиши "выход"
# # """)
#         print(f"{command}: {product[command]}")
#         if command == "выход":
#             break
#     except KeyError:
#         print("нет такой команды")

#—------------------------------- Задача —--------------------------------#

# #
# # дан JSON файл. Напиши CLI для получение информации о самом дорогом товаре, показа всех товаров из одинаковой категории
# # ПРИМЕР файла
# #
# # {
# #   "список_желаемого": [
# #     {
# #       "название": "Смартфон",
# #       "цена": 500,
# #       "категория": "Электроника"
# #     },
# #     {
# #       "название": "Наушники",
# #       "цена": 150,
# #       "категория": "Электроника"
# #     },
# #     {
# #       "название": "Книга",
# #       "цена": 20,
# #       "категория": "Литература"
# #     }
# #   ]
# # }
# import json
# with open("products.json", encoding="utf8") as f:
#     products = json.load(f)
# print(products['список_желаемого'])
# # products['список_желаемого'] -> [{}, {}, {}]
# # products['список_желаемого'][0]-> {}
# # products['список_желаемого'][0]['цена'] -> 500 (для примера)
# max_cost = -10000000000
# expensive_item = {}
# for product in products['список_желаемого']:
#     if product['цена'] > max_cost:
#         max_cost = product['цена']
#         expensive_item = product
# print(expensive_item)



