# # ---------------------------------------------- Задача --------------------------------------------------------------
# # Создать класс Book с атрибутами title, author, status ("в наличии" или "выдана") и методом display_info(),
# # который выводит информацию о книге. Создайте дочерний класс BorrowableBook, который наследует от класса Book.
# # Добавьте атрибут borrower (заимствовавший книгу) и методы borrow_book(user) и return_book(),
# # которые позволяют пользователю взять книгу в библиотеке и вернуть ее после использования.
#
# class Book:
#     def __init__(self):
#         self.__title = 'Martin Eden'
#         self.__author = 'Jack London'
#         self.__status = 'в наличии'
#
#     @property
#     def status(self):
#         return self.__status
#
#     @status.setter
#     def status(self, new_status):
#         self.__status = new_status
#     def display_info(self):
#         print(f'Книга: {self.__title}, Автор: {self.__author}, Статус: {self.__status}.')
#
#
#
#
# class User(Book):
#     def __init__(self, name):
#         super().__init__()
#         self.__name = name
#     def borrow_book(self, status):
#         self.status = status
#     def display_info(self):
#         super().display_info()
#         print(f'Name: {self.__name}.')
#
# book = Book()
# book.display_info()
#
# user = User('Ivan')
# user.borrow_book('взял') #user.status = 'взял'
# user.display_info()
#





















#
#
# #------------------------------------Магические методы---------------------------------#
# # Магические - перегрузки (равнозначные) #dunder methods
# # это назначения нового функционал к уже существующему оператору
#
# class Triangle:
#     def __init__(self, a, b, c): # __init__ - это пример магического метода
#         self.a = a
#         self.b = b
#         self.c = c
#
#     # def equals_triangles(self, other_triangle):
#     #     return self.a == other_triangle.a and self.b == other_triangle.b and self.c == other_triangle.c
#
#     # перегрузка оператора сравнения (==)
#     def __eq__(self, other_triangle): #->bool
#         return self.a == other_triangle.a and self.b == other_triangle.b and self.c == other_triangle.c
#
#
# triangle1 = Triangle(1,1,1)
# triangle2 = Triangle(1,2,1)
# print(triangle1)
# print(triangle2)
# print(triangle1 == triangle2)#print(triangle1.equals_triangles(triangle2)) #



# #—------------------------------- Задача —--------------------------------#
# # Создайте класс Vector, представляющий трехмерный вектор.
# # Реализуйте перегрузку оператора сложения(__add__(self, other)) для векторов так,
# # чтобы при сложении двух векторов получался новый вектор
# # с соответствующими суммированными координатами.
#
# #перегрузку оператора сложения(__add__(self, other)) -> return Vector
# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     # def __add__(self, other): #-> return Vector
#     #     new_x = self.x + other.x
#     #     new_y = self.y + other.y
#     #     new_z = self.z + other.z
#     #     return Vector(new_x, new_y, new_z)
#
#     def __add__(self, other):
#         if isinstance(other, Vector): # other == Vector
#             return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __str__(self): # return str
#         return f"Vector({self.x}, {self.y}, {self.z})"
#
# vector1 = Vector(1, 1, 1)
# vector2 = Vector(2, 2, 2)
# vector3 = vector1 + vector2
# print(vector3) # Vector(3, 3, 3)  видим потому что перегрузили str()



# #—------------------------------- Задача —--------------------------------#
#Создайте список таких треугольников. Необходимо найти самый маленький по площади треугольник.
# возможность вычисление площадей треугольник через сложение:
# треугольник.S + треугольник.S = треугольник.S+S # ТАК ДЕЛАТЬ не стоит :)
class Triangle:
    def __init__(self, a=0, b=0, c=0): # __init__ - это пример магического метода
        self.a = a
        self.b = b
        self.c = c
        self.S = self.s(a, b, c)

    def s(self, a, b, c):
        p = (a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))**0.5 #'реализация'

    # def equals_triangles(self, other_triangle):
    #     return self.a == other_triangle.a and self.b == other_triangle.b and self.c == other_triangle.c

    def __gt__(self, other):
        if isinstance(other, Triangle):
            return self.S > other.S

    def __add__(self, other):
        if isinstance(other, Triangle):
            result = Triangle()
            result.S = self.S + other.S
            return result
    # перегрузка оператора сравнения (==)
    def __eq__(self, other_triangle): #->bool
        return self.a == other_triangle.a and self.b == other_triangle.b and self.c == other_triangle.c
    def __str__(self):
        return f'S: {self.S}'

triangle1 = Triangle(1,1,1)
triangle2 = Triangle(2,2,2)
print(triangle1.S, triangle2.S, triangle1 > triangle2)
print(min(triangle1, triangle2))
print(triangle1+triangle2)