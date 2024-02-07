# class MyClass:
#     def __init__(self, attr1, attr2):
#         self.attr1 = [attr1]
#         self.attr2 = [attr2]
#
# #    def __delattr__(self, name):
#         # delattr(self, name)
#         # if name == 'attr1' or name == 'attr2':
#         #     delattr(self, name)
#         # else:
#         #     raise AttributeError("Не удаётся удалить атрибут")
#
#
# # Пример использования
# obj = MyClass(10, 20)
# print(obj.attr1, obj.attr2)  # Выведет: 10 20
# print(obj.__dict__)
# obj.__dict__.pop('attr2')
#
# print(obj.__dict__)
#
# # del obj.attr1
# # print(hasattr(obj, 'attr1'))  # Выведет: False
# #
# # del obj.attr2
# # print(hasattr(obj, 'attr2'))  # Выведет: False

# -------------------------------------Удаление из коллекции----------------------------------------- #
# class A:
#     ID = 0
#     def __init__(self):
#         self.a = 'class A'
#         A.ID += 1
#         self.id = A.ID
#     def __repr__(self):
#         return f'object of class A id: {self.id}'
# class MyContainer(object):
#
#     def __init__(self,*value):
#         self.storage = list(value)#{'one': 1}
#         self.storage2 = [6, 7, 8]
#
#     def __delitem__(self, key):
#         del self.storage[key]
#         del self.storage2[key]
#
# container = MyContainer(A(),A(),A())
#
# print(container.__dict__) #
# del container[None]
# print(container.__dict__) #
#del container['one']  # KeyError: 'one'



# ----------------------------------------------------------------------------------- #
# # # ---------------------------модульные тесты-------------------------------------- #
# # # это специальные функции, которые тестируют ваш модуль, чаще всего описывают тест кейсы
# import pytest
# '''
# Проверка, является ли год високосным
# @param [in] year - год для проверки
# @return bool - True, если год високосный, и False в противном случае
# '''
# def is_leap_year(year: int) -> bool:
#    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
# def test_is_leap_base_test():
#     # case  is_leap
#     # значение / ожидание / фактический результат
#     # 2024   / True      /
#     expected_result = True
#     actual_result = is_leap_year(2024)
#     assert expected_result == actual_result # ожидание == реальность?
#
# def test_is_leap_not_loop_year():
#     # case  is_leap
#     # значение / ожидание / фактический результат
#     # 2023   / False      /
#     expected_result = False
#     actual_result = is_leap_year(2023)
#     assert expected_result == actual_result # ожидание == реальность?
#
# def test_is_leap_negative_year():
#     # case  is_leap
#     # значение / ожидание / фактический результат
#     # -2023   / False      /
#     expected_result = False
#     actual_result = is_leap_year(-2023)
#     assert expected_result == actual_result # ожидание == реальность?
#
#

#
# # #-----------------------задача---------------------------------#
# # Описание: Напишите функцию,
# # которая принимает длины всех трех сторон треугольника и
# # возвращает его площадь, используя формулу Герона.
#
# # Если треугольника не существует, то функция должна возвращать -1
#
# def triangle_area(a, b, c):
#     s = (a + b + c) / 2
#     return (s * (s - a) * (s - b) * (s - c)) ** 0.5
#
#
# def test_triangle_area_base():
#     expected_result = 3.9 #хотим вычислить площадь 3, 3, 3
#     actual_result = triangle_area(3,3,3)
#     assert expected_result == round(actual_result,1)
#
# def test_triangle_area_does_not_exist():# функция показала наличие ошибок в triangle_area
#     expected_result = -1 #хотим вычислить площадь 1, 2, 4
#     actual_result = triangle_area(1,2,4)
#     assert actual_result == expected_result
#
# def test_triangle_area_negative_side():# функция показала наличие ошибок в triangle_area
#     expected_result = -1 #хотим вычислить площадь -3, -3, -3
#     actual_result = triangle_area(-3,-3,-3)
#     assert actual_result == expected_result



# # --------------------------задача--------------------------- #
# # Площадь прямоугольника:
# # функция, которая принимает длину и ширину прямоугольника и возвращает его площадь.
# # Если прямоугольника не существует, то функция должна возвращать -1
def rectangle_area(length, width):
    return length * width


# def test_rectangle_area():
#     excepted_result = 50
#     actual_result = rectangle_area(10, 5)
#     assert actual_result == excepted_result
#
# def test_rectangle_area_negative_numbers():
#     excepted_result = -1
#     actual_result = rectangle_area(-10, -5)
#     assert actual_result == excepted_result
#
# def test_rectangle_area_zero_side():
#     excepted_result = -1
#     actual_result = rectangle_area(0, 5)
#     assert actual_result == excepted_result
#
# def test_rectangle_area_strin_numbers():
#     excepted_result = -1
#     actual_result = rectangle_area('10', 5)
#     assert actual_result == excepted_result



#--------------------параматрезация---------------------------#
import  pytest
# [(тестовые данные), (тестовые данные), ...]
@pytest.mark.parametrize("width, height, expected",
                         [(10, 5, 50),
                          (-10, -5, -1),
                          (0, 10, -1),
                          ("10", 5, -1)])
def test_rectangle_area_strin_numbers(width, height, expected):
    expected_result = expected
    actual_result = rectangle_area(width, height)
    assert actual_result == expected_result




