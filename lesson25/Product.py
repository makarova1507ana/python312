from functools import reduce


#—------------------------------- Задача —--------------------------------#
# Создайте класс, представляющий товар или продукт, хранящий информацию о его названии,
# цене и добавьте методы просмотр товара
# создайте список таких товаров. Необходимо найти самый дорогой товар
class Product:
    def __init__(self, name, price): #Основная задача: завершить создание объект (запись данных в поля класса и т.д.)
        #print("сработал метод init")
        self.name = name
        self.price = self.valid_price(price)

    @staticmethod
    def valid_price(price):
        if price > 0:
            return price
        raise "недопустимая стоимость"


    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price

    # def __add__(self, other): #-> {'products': [p1, p2], 'finally_price': 1000 }
    #     products = [self.name, other.name]
    #     finally_price = self.price + other.price
    #     return {'products': products, 'finally_price': finally_price}
    def __add__(self, other): #-> Product
        if isinstance(other, Product):
            return Product('корзина', self.price + other.price)

    def __str__(self):
       return f'Product: {self.name}, price: {self.price}'

# product1 = Product('product1', 1000, 150)
# product2 = Product('product2', 700, 100)

# if product1 < product2:
#     print("product1 стоит меньше чем product2")
# else:
#     print("product1 стоит больше чем или равно product2")
products = [Product("product1", 1000),
            Product("product2", 700),
            Product("product3", 550),
            Product("product3", 100)]
print(max(products))
print(min(products))
#print(products[0] + products[1] + products[2])
result = reduce(lambda product1, product2: product1 + product2, products)
print(result)


# for product in products:
#     product.show_product()

# #
# class Pizza(Product):
#     def __init__(self, name, price, quantity, size):
#         super().__init__(name, price, quantity) #super() - это специальный объект позволяет обратиться к родительскому класса
#         self.size = size
#
#     @staticmethod
#     def valid_size(size):
#         if size in ["small", "medium", "big"]:
#             return size
#         raise "недопустимый размер пиццы"
#
# product = Product("cheese_cake", 100, 1000)
# product.show_product()
# pizza = Pizza("margarita", -500,1200, "small")
# pizza.show_product()
# print(pizza.size)
#
# # Создать список общих продуктов и список пицц и узнать самый дорогой продукт