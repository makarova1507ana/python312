# Необходимо реализовать следующее:
# Создать класс NewYearDecoration с атрибутами: name (название украшения), price (цена), quantity (количество на складе).
# Метод display_info() для просмотра информации об украшении (название, цена, количество на складе).
# Методы edit_price(new_price) и edit_quantity(new_quantity) для изменения цены и количества украшения соответственно.
class NewYearDecoration:
    def __init__(self, name: str, price: float, quantity: int):

        self.__name = name
        self.__price = price if self.is_valid_price(price) else 0
        self.__quantity = quantity if self.is_valid_quantity(quantity) else 0

    def is_valid_quantity(self, quantity):
        return type(quantity) == int and quantity >= 0
    def is_valid_price(self, price):
        return (type(price) == int or type(price) == float) and price >= 0
            # self.__price = 0  # либо этот вариант, либо raise
            # # raise "error price < 0" #прерывает работу всей программы

    def display_info(self): #Читаем(узнаем) информацию
        return f"name: {self.__name}\nprice: {self.__price}\nquantity: {self.__quantity}"

    def edit_price(self, discount: float, new_price: float = None):
        #print(f"discount: {discount}, new_price: {new_price}")
        # Если есть скидка > 0, то назначаем новую стоимость с учетом скидки

        if discount > 0:
            self.__price = self.__price * (1 - discount/100)
        elif self.is_valid_price(new_price):# если discount = 0 или меньше, то смотрим чтобы new_price != None
            self.__price = new_price
        # иначе стоимость оставить прежней

    def edit_quantity(self, new_quantity):
        if self.is_valid_quantity(new_quantity):
            self.__quantity = new_quantity

        #print(f"new_quantity: {new_quantity}")
