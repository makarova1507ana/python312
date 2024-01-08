

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
        self.__name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name
    def show_product(self):
        print(f'Product: {self.__name}, price: {self.price}, quantity: {self.quantity}')

#

# pizza = Product(name='Pepperoni', price=850, quantity=3)
# pizza.show_product()

#так делать не стоит
#print(pizza._Product__name) # private name но видим значение в этом поле


# # так лучше
# print(pizza.get_name())






#—------------------------------- Задача —--------------------------------#
# Создайте класс, представляющий Cat,
# хранящий информацию о его кличке, настроение, энергию (nickname, mood, energy ) и
# добавьте методы для редактирование этих параметров
# игрок при создание персонажа должен задать только кличку,
# а параметры настроение, энергию задаются автоматически и равны 100
class Cat:
    def __init__(self, nickname: str):
        self.__nickname = self.validate_nickname(nickname)
        self.__mood = 100
        self.__energy = 100

    # декоратор - @decorate_future  -> добавляют новое поведение(функционал) вашей функции
    @staticmethod # не использовать объект класса, но позволит использовать пространство класса
    def validate_nickname(nickname):
        if type(nickname) != str:
            raise "nickname must be str" # ошибка для разработчика
        if len(nickname) < 5:
            raise "nickaname's length must be 5 or more symbols" # raise можно поймать через try except
        if nickname.isspace():
            raise "must not be only space symbols"
        return nickname
    def get_nickname(self):# геттер - метод, в котором я данные могу только читать
        return self.__nickname
    def set_nickname(self, nickname): # сеттер - метод, в кото
        self.__nickname = self.validate_nickname(nickname)

    @property # позволяет обращаться как к атрибуту класса(cat.mood), а не как к методу (cat.mood())
    def mood(self):
        return self.__mood

    @mood.setter # позволяет обращаться по такому примеру cat.mood = value
    def mood(self, mood):
        self.__mood = mood



cat = Cat("Vasya") #здесь происходит создание объекта
print(cat.get_nickname())
# cat.set_nickname("V") # не можем поменять, так как в сеттере тоже используем проверку и она не проходит
# print(cat.get_nickname())

try:
    Cat.validate_nickname("v") # Cat - не объект, а пространство
    print("Валидное имя")
except:
    print("Не валидное имя")

print(cat.mood) # вызваю геттер
cat.mood = 150  # вызваю сеттер вместо cat.set_mood(150)
print(cat.mood)