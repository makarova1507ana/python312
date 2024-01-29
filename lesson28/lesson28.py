# # # ---------------------------------------Множественное наследование------------------------------------------------- #
# # class A:
# #     pass
# #
# # class B:
# #     pass
# #
# # class C(A, B): #Множественное наследование
# #     pass
# # # ----------------------------------------------------------------#
# # class Goods:
# #     def __init__(self, name, price):
# #         super().__init__() #вызываен init MixinLog
# #         print("init Goods")
# #         self.name = name
# #         self.price = price
# #
# #     def __str__(self):
# #         return f"name: {self.name}  price: {self.price}"
# #
# # class MixinLog:#учет товаров
# #     ID = 0 # общая для всех объектов этого класса
# #     def __init__(self):
# #         print("init MixinLog")
# #         MixinLog.ID += 1
# #         self.id = MixinLog.ID
# #     def __str__(self):
# #         return f"id: {self.id}"
# # class NoteBook(Goods, MixinLog):
# #     def __str__(self):
# #         return 'goods: ' + Goods.__str__(self) + ' | mixinglog ' + MixinLog.__str__(self)
# #
# #
# #
# # # good = Goods('good1', 1000)
# # # print(good)
# #
# # notebook = NoteBook('notebook1', 500)
# # print(notebook)
# # print(MixinLog.ID)
# #
# # notebook2 = NoteBook('notebook2', 600)
# # print(notebook2)#, 'id:', notebook2.id)
# # print(MixinLog.ID)
#
#
# # -------------------------------коллекция __slots__ ----------------------------------------- #
# # 1. нужна для ограничения создаваемых свойств у класса (или его экземпляра)
# # 2. уменьшение занимаемой памяти для экземпляров класса
# # 3. для ускорения работы с локальными свойствами
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.y = y
#     def calc(self):
#         return str(self.__x + self.y)
# point = Point(5, 3)
# point2 = Point(-1, 32)
# print(point.__dict__, point2.__dict__)
# point.__dict__['_Point__x'] = 111 # !!!
# print(point.__dict__, point2.__dict__)
# point.__dict__['my ney key'] = 'value'# !!!
# print(point.__dict__, point2.__dict__)
#
#
# class Point3D:
#     __slots__ = ('__x', 'y') # кортеж
#     def __init__(self, x, y):
#         self.__x = x
#         self.y = y
#
#     def calc(self):
#         return str(self.__x + self.y)
#
# point3d = Point3D(34, 22)
# #print(point3d.__dict__) #Ошибка потому что определели __slots__
# print(point3d.__slots__)
# #point3d.__slots__[0] = 8 # 'tuple' object does not support item assignment
# #point3d.__slots__ = ('yyy', 'xxx') # AttributeError: 'Point3D' object attribute '__slots__' is read-only
#
# # #2. уменьшение занимаемой памяти для экземпляров класса
# # print('size of memory: ', point.__sizeof__() + point.__dict__.__sizeof__())
# # print('size of memory: ', point3d.__sizeof__() + point3d.__slots__.__sizeof__())
#
# # # 3. для ускорения работы с локальными свойствами
# # import timeit
# # import time
# # time1 = timeit.timeit(point.calc())
# # time2 = timeit.timeit(point.calc())
# # time.sleep(5)
# # time3 = timeit.timeit(point3d.calc())
# # time4 = timeit.timeit(point3d.calc())
# #
# # print(time1, time2, time3, time4)
#



# # ------------------------------------Расширение и Переопределение методов при наследование --------------------------------------- #
# from abc import ABC, abstractmethod
# class A(ABC):
#     def method(self):
#         pass
#     @abstractmethod
#     def absctactmethod(self):
#         print('this is absctactmethod in class A')
#
# class B(A):
#     def absctactmethod(self): # переопределением метода из базового класса A
#         print('this is absctactmethod in class B')
#
# class C(A):
#     def absctactmethod(self): # расширение метода из базового класса A
#         super().absctactmethod()
#         print('in class C')
# b = B()
# b.absctactmethod()
# c = C()
# c.absctactmethod()






# # ---------------------------------Интерфейсы при наследование------------------------------------------ #
# # Интерфейсы: Способы взаимодействия с объектами, определяющие,
# # какие методы могут быть использованы с объектами определенного класса.
#
# # Интерфейс == абстрактный класс, у которого все методы абстракные (ДОГОВОРЕННОСТЬ)
#
# from abc import ABC, abstractmethod
# # класс должен быть абстрактным
# # Все методы абстрактные
# class Interface(ABC):
#     @abstractmethod
#     def method1(self):
#         pass
#
#     @abstractmethod
#     def method2(self):
#         pass



#------------------задача в файле shop/main.py-------------#