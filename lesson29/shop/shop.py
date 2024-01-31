# класс магазин (имя, список товаров) методы: просмотр имя, список \ добавлять/удалять/редактирвоать товары
from good import Good
class Shop:
    __slots__ = ('__name', '__goods')

    '''
    @param goods: list - список товаров -> [Good(), Good()...]
    '''
    def __init__(self, name: str, *goods: tuple):
        if type(name) != str:
            raise 'name is not string'
        if not(type(goods) in [set, tuple, list]):
            raise 'goods is not list'


        self.__name = name
        self.__goods = list(goods)

    def __str__(self):
        goods = list(map(lambda el: str(el), self.__goods))
        result = '\n-*- '.join(goods)
        return f'name: {self.__name} \n-*- '+ result

    @property
    def name(self):
        return self.__name

    @property
    def goods(self):
        return self.__goods

    @goods.setter # Добавление товаров в магазин (в список магазина)
    def goods(self, *goods):# *goods = () -кортеж в котором могут быть переданы от 0 до бесконечности аргументов
        for good in goods:
            if type(good) != Good:
                raise "должен быть товар"
            self.__goods.append(good)


# for good in shop.goods:
#     print(good)

