
#—------------------------------- Задача —--------------------------------#
# Создайте класс, представляющий товар или продукт, хранящий информацию о его названии,
# цене, количестве на складе и добавьте методы просмотр товара
class Product:
    def __init__(self, name, price, quantity): #Основная задача: завершить создание объект (запись данных в поля класса и т.д.)
        #print("сработал метод init")
        self.name = name
        self.price = self.valid_price(price)
        self.quantity = quantity

    @staticmethod
    def valid_price(price):
        if price > 0:
            return price
        raise "недопустимая стоимость"
    def show_product(self):
        print(f'Product: {self.name}, price: {self.price}, quantity: {self.quantity}')

#
class Pizza(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity) #super() - это специальный объект позволяет обратиться к родительскому класса
        self.size = size

    @staticmethod
    def valid_size(size):
        if size in ["small", "medium", "big"]:
            return size
        raise "недопустимый размер пиццы"

product = Product("cheese_cake", 100, 1000)
product.show_product()
pizza = Pizza("margarita", -500,1200, "small")
pizza.show_product()
print(pizza.size)

# Создать список общих продуктов и список пицц и узнать самый дорогой продукт