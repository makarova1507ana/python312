# класс товары
# товар(имя, цена, кол-во в магазине) методы: чтение имени, цены, кол-во.
# редактировать цену, кол-во
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
        raise "value < 0"

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