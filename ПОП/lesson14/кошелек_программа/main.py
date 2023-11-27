# # основная программа и ее интерфейс
#
#
# #—------------------------------- Задача —--------------------------------#
# # Кошелек.
# # Реализовать интерфейс для управления кошельком.
# # Доступные функции:
# # Просмотр баланса
# # Снятие
# # Пополнение
#
#
#
# import wallet  # или так from wallet import refill, ...
#
#
#
# balance = 100
# def menu(command):
#     global balance #функция menu теперь обращается именно области памяти  в 18 строке
#     if command == "1":
#         return print(f"Ваш баланс: {balance}")
#     money = input("введите желамую сумму")
#     if command == "2": balance = wallet.refill(balance, money)
#     if command == "3": balance = wallet.withdrawal(balance, money)




# user_command = 1
#
# while user_command != "0":# точка входа
#     user_command = input("""
# - выход из программы нажмите 0
# - Просмотр баланса нажмите 1
# - Пополнение нажмите 2
# - Снятие нажмите  3
# """)
#
#     try:
#         menu(user_command)
#     except:
#         print("error command")
#

#
# from wallet import *
#
#
#
# balance = 100
#
# commands = {# "1": print(f"Ваш баланс: {balance}")
# "2": refill, # потенциальна можно, но
# "3": withdrawal}
#

# user_command = 1
# money = 100
# while user_command != "0":# точка входа
#     user_command = input("""
# - выход из программы нажмите 0
# - Просмотр баланса нажмите 1
# - Пополнение нажмите 2
# - Снятие нажмите  3
# """)
#
#     try:
#         commands(balance, money)
#     except:
#         print("error command")