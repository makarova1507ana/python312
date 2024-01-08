# класс - (можно сравнить) тип данных
# объект - переменная со значением

#
# # age - переменная, значение = 34, а тип данных int
# age = 34
# print(type(age))
# # age - объект , класса int





# класс - это пользовательский (который вы определили сами) тип данных

# Cat - это класс (шаблон, по которому я могу создать любого кота)
# class Cat:
#     # инициализатор - это специальная функция, которая создает объект
#     def __init__(self, name, age): # self - это указатель на конкретный объект
#         self.name = name #   self.name  - поле класса (== свойство ==атрибут класса)
#         self.age = age #   self.age  - поле класса (== свойство ==атрибут класса)



# # Создаем объект(== экземпляр) класс Cat
# my_cat = Cat(name="Barsik", age=2) #my_cat - это объект
# print(f"name: {my_cat.name}, age: {my_cat.age}")
#
# freinds_cat = Cat(name="Vasya", age=5) #freinds_cat - это объект
# print(f"name: {freinds_cat.name}, age: {freinds_cat.age}")




#—------------------------------- Задача —--------------------------------#
#Создайте класс Автомобиль, который содержит информацию о марке, модели, годе выпуска
class Auto:
    def __init__(self, brand, model, year):
        self.brand = brand #
        self.model = model
        self.year = year


# my_auto = Auto(brand='BMW', model='X5', year=2013)
# print(f'My auto: brand - {my_auto.brand}, model - {my_auto.model}, year of issue - {my_auto.year}.')







#Инкапсуляция - сокрытие данных, методов, настраивается через модификаторы доступа

# модификаторы доступа:
# self.name: public - открытый (по умолчанию)
# self._name: protected - защищенный (используется при наследование)
# self.__name: private - закрытый (нельзя получать данные не из класса)
class Cat:
    # инициализатор - это специальная функция, которая создает объект
    def __init__(self, name, age): # self - это указатель на конкретный объект
        self.__name = name
        self.__age = age
        self.__health = 100

    def get_name(self): #геттер - получить данные об закрытом атрибуте
        return self.__name

    def get_age(self):
        return self.__age

    def get_health(self):
        return self.__health

    def show_cat(self):
        print(f"name: {self.get_name()}, age: {self.get_age()}, health: {self.get_health()}")

    def hit(self): # это функция, НО называется МЕТОД, потому что ВНУТРИ класса
        self.__health -= 10

# my_cat = Cat("Barsik", 2)
# my_cat.show_cat()
# my_cat.health = '0'
# my_cat.hit()
# my_cat.show_cat()


#—------------------------------- Задача —--------------------------------#
# Создайте класс, представляющий товар или продукт, хранящий информацию о его названии,
# цене, количестве на складе и добавьте методы просмотр товара
class Product:
    # __new__ -> конструктор -> создает объект -> выделить область памяти
    # def __new__(cls, name, price, quantity): # Основная задача: выделить область памяти
    #     print("сработал метод new")
    #     return super().__new__(cls) # вернемся при изучении наследования

    def __init__(self, name, price, quantity): #Основная задача: завершить создание объект (запись данных в поля класса и т.д.)
        #print("сработал метод init")
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_product(self):
        print(f'Product: {self.name}, price: {self.price}, quantity: {self.quantity}')

#

pizza = Product(name='Pepperoni', price=850, quantity=3)
pizza.show_product()

print(pizza.name)



















