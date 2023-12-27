# #—------------------------------- Задача —--------------------------------#
# # Создайте класс NewYearDecoration, представляющий новогодние украшения в магазине.
# # Каждое украшение хранит информацию о своем названии, цене и количестве на складе.
#
from NewYearDecoration import NewYearDecoration
new_year_tree = NewYearDecoration('New year tree', 10000, 40)
print(new_year_tree.display_info())

# edit_price()
print("-----------------АДМИН ПАНЕЛЬ----------------------")
while True:
    command = input("""
1 - показать информацию о товаре
2 - отредактировать стоимость
3 - отредактировать количествo
4 - выход
""")
    if command == "4":
        print("------------------выход---------------------")
        break
    elif command == "1":
        print("------------------показать информацию о товаре---------------------")
        print(new_year_tree.display_info())
    elif command == "2":
        print("------------------отредактировать стоимость---------------------")
        discount = int(input("Введите скидку товара: "))
        new_price = input("Введите новую стоимость товара: ")
        new_price = None if new_price == '' else int(new_price)  # Если ничего не ввели, то определим None
        new_year_tree.edit_price(discount=discount, new_price=new_price)
    elif command == "3":
        print("------------------отредактировать количествo---------------------")
        quantity = int(input("Введите количествo"))
        new_year_tree.edit_quantity(quantity)
    else:
        print("error command")
