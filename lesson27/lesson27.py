# #-----------------------------------Абстрактный класс----------------------------------------------#
# # Абстрактный класс - это такой класс, у которого нельзя(не предполагает ) создавать экземпляры класса
# # Базовый класс - это такой начальный класс, от которого идет наследование
# from accessify import private, protected
# class A: # Базовый класс
#     # private - доступен только самому классу
#     # protected - доступна классу и классам наследникам
#     # public - доступ всем и всегда (и самому классу, и классу наследнику, и вне класса в любом другом вместе, и т.д.)
#     def __init__(self):
#         self.__private_a = "private_a"
#         self._protected_a = "protected_a"
#         self.public_a = "public_a"
#
#     @private
#     def __private_methodA(self):#договрились, что можем использовать только здесь
#         return "private methodA"
#     @protected
#     def _protected_methodA(self): #договрились, что можем использовать у наследников
#         return "protected methodA"
#     def public_methodA(self):#договрились, что можем использовать где хотим
#         return "public methodA"
# class B(A):
#     def methodB(self):
#         return f"methodB {self.public_a} {self._protected_a} {self.__private_a}"
# class C(B):
#     def methodC(self):
#         return "methodC"
#
# a = A()
# print(a.public_a)
# print(a.public_methodA())
# print(a._protected_methodA)
# b = B()
# print(b.methodB())
# print(b._protected_methodA)

#
# # пример
# # представим, что нам надо создать приложения для рисования геометрических фигур
# # Какой класс будет базовым ?
# # Обязательность определения метода draw
# from abc import ABC, abstractmethod
# class Figure(ABC): # Абстрактный класс
#     def __init__(self, color: str):
#         self._color = color
#     @abstractmethod #метод, который должен быть определен у классов наследников
#     def draw(self):
#         print(f"Draw some figure")
#
# class Square(Figure):
#     def __init__(self, a: float,  color: str):
#         super().__init__(color)
#         self._a = a
#     def draw(self):
#         super().draw()
#         print(f"Draw Square a: {self._a}, color: {self._color}")
#
# class Rectangle(Square):
#     def __init__(self, a: float, b: float,  color: str):
#         super().__init__(a, color)
#         self.__b = b
#     def draw(self):
#         print(f"Draw Rectangle a: {self._a} b: {self.__b} , color: {self._color}")
#
# class Parallelogram(Figure):
#     def __init__(self, a: float, b: float, angle: float, color: str):
#         super().__init__(color)
#         self.__a = a
#         self.__b = b
#         self.__angle = angle
#     def draw(self): # реализация рисования значительно отличается от остальных классов
#         print(f"Draw Parallelogram a: {self.__a} b: {self.__b} angle: {self.__angle}, color: {self._color}")
#
# # figure = Figure('red') # не получиться экземпляр класс, потому  Figure - абстрактный класс
# # figure.draw() #
#
# print("-------------------------------")
# square = Square(5, 'red')
# square.draw()
#
# print("-------------------------------")
# rectangle = Rectangle(5, 10, 'red')
# rectangle.draw()
#
#
# print("-------------------------------")
# figures = [rectangle, square, rectangle, square, Parallelogram(3, 5, 30, 'black')]
# for figure in figures:
#     figure.draw()
#



#—------------------------------- Задача —--------------------------------#
# Реализуйте систему банковских счетов с использованием наследования.
# Создайте базовый-абстрактный класс, а затем подклассы, представляющие "Текущий счет",
# "Сберегательный счет"(деньги снять нельзя, но они увеличиваются на определенный процент каждый год) и
# "Кредитный счет"(можно снять деньги, но будет специальный атрибут долг, который будет расти каждый год на орпеделенный процент).
# Реализуйте методы для внесения и снятия средств.


# Создайте базовый-абстрактный класс Счет
# * метод пополнения
# * метод просмотра
# * метод снятия
#
# класс "Текущий счет"
# * метод пополнения
# * метод просмотра
# * метод снятия

# "Сберегательный счет"(деньги снять можно по истечению конкретного срока, но они увеличиваются на определенный процент каждый год) и
# * метод пополнения
# * метод просмотра
# * метод снятия (подумать над правилами)

# "Кредитный счет"(можно снять деньги, но будет специальный атрибут долг, который будет расти каждый год на орпеделенный процент).
# * метод пополнения
# * метод просмотра
# * метод снятия


from abc import ABC, abstractmethod


class Account(ABC):

    @staticmethod
    def _is_money(money):
        if not((type(money) in [float, int]) and money > 0):
            raise "Передаваемая сумма меньше 0 или не int или не float"

    @abstractmethod
    def add(self, money):
        pass

    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def withdraw(self, money):
        pass


class ActiveAccount(Account):

    def __init__(self):
        self._balance = 0

    def add(self, money):
        self._is_money(money)
        self._balance += money
        return self._balance

    def view(self):
        return self._balance

    def withdraw(self, money):
        self._is_money(money)
        if self._balance < money:
            raise ValueError('не хватает денег на балансе')

        self._balance -= money
        return self._balance

user_account = ActiveAccount()
user_account.add(-100)
print(user_account.view())