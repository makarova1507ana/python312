# класс товары
# товар(имя, цена, кол-во в магазине) методы: чтение имени, цены, кол-во.
# редактировать цену, кол-во
class InvalidAttribute(Exception):
    ''''''
    def __str__(self):
        return f'Ошибка: value < 0'
class Good:
    __slots__ = ('__name', '__price', '__count')

    def __init__(self, name: str, price: float = 0, count: float = 0):
        if type(name) != str:
            raise 'name is not string'

        self.__name = name
        self.__price = self.isValidAttribute(price)
        self.__count = self.isValidAttribute(count)
    @staticmethod
    def isValidAttribute(value):
        if type(value) in [int, float] and value >= 0:
            return value
        raise InvalidAttribute #ссылаемся на наш класс-исключение

    def __str__(self):
        return f"name: {self.__name} | price: {self.__price} | count: {self.__count}"

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = self.isValidAttribute(price)

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = self.isValidAttribute(count)


#Создание товаров
def createGood():
    goods = []
    while True:
        stop = input('Хотите добавить товар? \nвведите д или н\n')
        if stop.lower() == 'н':
            break
        name_good = input('Введите имя товара: ')
        price_good = input('Введите стоимость товара: ')
        count_good = int(input('Введите кол-во товара в магазине: '))

        ''' надо добавить обработку входных price_good  & count_good'''
        try:
            price_good = float(price_good)
        except:
            #что-то предпринять для ликвидаии проблемы
            pass
        good = Good(name_good, price_good, count_good)
        goods.append(good)
    return goods

createGood()