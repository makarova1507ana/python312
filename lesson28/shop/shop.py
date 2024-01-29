# класс магазин (имя, список товаров) методы: просмотр имя, список \ добавлять/удалять/редактирвоать товары
from good import Good
class Shop:
    __slots__ = ('__name', '__goods')

    '''
    @param goods: list - список товаров -> [Good(), Good()...]
    '''
    def __init__(self, name: str, goods: list):
        if type(name) != str:
            raise 'name is not string'
        if type(goods) != list:
            if not(type(goods) in [set, tuple]):
                raise 'goods is not list'
            goods = list(goods)

        self.__name = name
        self.__goods = goods

    def __str__(self):
        goods = list(map(lambda el: str(el), self.__goods))
        result = ' -*- '.join(goods)
        return f'name: {self.__name} -*- '+ result

    @property
    def name(self):
        return self.__name

    @property
    def goods(self):
        return self.__goods

shop = Shop('shop', [Good('good1',100, 110), Good('good2',200, 310)])
print(shop)
print(shop.goods)