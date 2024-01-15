import tkinter as tk
from NewYearDecoration import NewYearDecoration
# Функция для отображения информации из полей ввода на метке
def show_info():
    # Получение информации из полей ввода
    name, price, quantity = entry_name.get(), entry_price.get(), entry_quantity.get()
    # создавать объект украшения
    new_year_tree = NewYearDecoration(name, int(price), int(quantity))

    # редактирование объекта new_year_tree
    if edit_price.get():
        new_price = int(edit_price.get())
        new_year_tree.edit_price(discount=0,new_price= new_price)
    if edit_quantity.get():
        new_quantity = int(edit_quantity.get())
        new_year_tree.edit_quantity(new_quantity)
    # Отображение информации на метке info_label
    info_label.config(text=new_year_tree.display_info())

# Создание главного окна
root = tk.Tk()
root.title("Форма с полями ввода")
root.minsize(300, 200)  # Устанавливаем минимальные размеры окна (ширина x высота)
root.maxsize(800, 600)  # Устанавливаем максимальные размеры окна (ширина x высота)
window_width = 400  # Ширина окна
window_height = 300  # Высота окна
screen_width = root.winfo_screenwidth()  # Получаем ширину экрана
screen_height = root.winfo_screenheight()  # Получаем высоту экрана

x_position = (screen_width - window_width) // 2  # Вычисляем положение окна по горизонтали
y_position = (screen_height - window_height) // 2  # Вычисляем положение окна по вертикали

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  # Устанавливаем размер и положение окна



# Описание полей ввода для имени, возраста и города
fields = [
    ("Имя:", tk.Entry(root)),
    ("Цена:", tk.Entry(root)),
    ("Кол-во:", tk.Entry(root))
]

# Создание и размещение меток и полей ввода на главном окне
for label_text, entry_widget in fields:
    tk.Label(root, text=label_text).pack()  # Создание метки с текстом из списка fields
    entry_widget.pack()  # Размещение поля ввода

# Доступ к полям ввода по переменным entry_name, entry_price и entry_quantity
entry_name, entry_price, entry_quantity = (field[1] for field in fields)

# Кнопка "Подтвердить", вызывает функцию show_info при нажатии
submit_button = tk.Button(root, text="Подтвердить", command=show_info)
submit_button.pack()

# Метка для отображения введенной информации
info_label = tk.Label(root, text="")
info_label.pack()


# edit_price
edit_price = tk.Entry(root, text="новая цена")
edit_price.pack()
submit_button = tk.Button(root, text="Изменить цену", command=show_info)
submit_button.pack()


# edit_quantity
edit_quantity = tk.Entry(root, text="новое кол-во")
edit_quantity.pack()
submit_button = tk.Button(root, text="Изменить кол-во", command=show_info)
submit_button.pack()




# Запуск главного цикла программы
root.mainloop()
