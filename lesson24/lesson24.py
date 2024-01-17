# # # статические методы и методы класса
#
# # Статические методы и методы класса
#
# # Статический метод
# class DataProcessor:
#     data_proccess = 1000
#     @staticmethod
#     def process_data(data):  # Стала обычной функцией
#         #print(cls.data_proccess) # нельзя так как статический метод
#         # обработка данных
#         return data
#
#
# # Метод класса
#
# class Account:
#     rate = 0.05  # общий аттрибут для всех экземпляров класса
#
#     def __init__(self):
#         self.__balance = self.valid_balance(1000)  # аттрибут принадлежит конкретному экземпляру класса
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, balance):
#         self.__balance = balance
#     @staticmethod
#     def valid_balance(balance):
#         # проверка баланаса
#         return balance
#
#     @classmethod
#     def apply_interest(cls, rate ):  # вычисление процентной ставки
#         cls.rate = rate # присвоит всем экземплярам одинаковое значение
#
#     @classmethod
#     def add_money(cls, money):  # добавление денег
#         cls.balance += money
#
# #
# # account_1 = Account()
# # account_2 = Account()
# # account_2.balance = 5000
# #
# # print('Начальные значения: ')
# # print('Account 1: ', account_1.rate, account_1.balance)
# # print('Account 2: ', account_2.rate, account_2.balance)
# #
# # print('\nМеняем для всех баланс при помощи метода класса: ')
# # Account.apply_interest(1000)
# # print('Account 1: ', account_1.rate, account_1.balance)
# # print('Account 2: ', account_2.rate, account_2.balance)
# #
# # print('\nДобавляем всем 500 рублей: ')
# # Account.add_money(500)
# # print('Account 1: ', account_1.rate, account_1.balance)
# # print('Account 2: ', account_2.rate, account_2.balance)
# #
# # account_1.balance = 5000
# # print('\nДобавляем всем 500 рублей: ')
# # Account.add_money(500)
# # print('Account 1: ', account_1.rate, account_1.balance)
# # print('Account 2: ', account_2.rate, account_2.balance)
# #
# # print('\nМеняем для всех аттрибут ставки: ')
# # Account.rate = 0.15
# # print('Account 1: ', account_1.rate, account_1.balance)
# # print('Account 2: ', account_2.rate, account_2.balance)
#
# # import random
# #
# # # практический пример Статические методы и методы класса
# # class Client:# клиент у мобильного оператора
# #     date_payment = "01.01.1900"
# #     code_operator = "+7 999"
# #     def __init__(self):
# #          self.phone_numbers = [self.create_phone_number(self.code_operator)] # множество номеров телефона у одного экзмепляра
# #
# #     @staticmethod
# #     def create_phone_number(code_operator):
# #         return code_operator + str(random.randint(1000000, 9999999))
# #
# #     def add_phone_number(self, phone_number):
# #         self.phone_numbers.append(phone_number)
# #
# #     @classmethod
# #     def change_date(cls, date=""):
# #         if date:
# #             cls.date_payment = date
# #         else:
# #             month = cls.date_payment[3:5]
# #             year = cls.date_payment[6:]
# #             if int(month) + 1 >= 13:
# #                 month = "01"
# #                 year = str(int(year) + 1)
# #             cls.date_payment = cls.date_payment[:3] + month + '.' + year
# #
# #
# # client1 = Client()
# # client2 = Client()
# #
# # print(client1.date_payment, client1.phone_numbers)
# # print(client2.date_payment, client2.phone_numbers)
# #
# # Client.change_date("01.12.2024")
# # print(client1.date_payment, client1.phone_numbers)
# # print(client2.date_payment, client2.phone_numbers)
# #
# # Client.change_date()
# # print(client1.date_payment, client1.phone_numbers)
# # print(client2.date_payment, client2.phone_numbers)
#
#
#
# # ------------------------------Наследование------------------------------------- #
# # передаче всех атрибутов методов в дочерний класс
#
#
# # Ролевая модель на сайт: сотрудник(есть ФИО, доступ к админ панели и к просмотру основого сайта),
# # пользователь (есть ФИО, доступ к просмотру основого сайта)
#
# class User: # родительский класс
#     def __init__(self, name):
#         self.name = name
#     def see_main_site(self):
#         print("see main site")
#
# class Staff(User): # дочерний класс
#     def see_admin_panel(self):
#         print("see admin panel")
#
# user = User("Ivan")
# print(user.name)
# user.see_main_site()
#
# admin = Staff("admin")
# print(admin.name)
# admin.see_main_site()
# admin.see_admin_panel()
