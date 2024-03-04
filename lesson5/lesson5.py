import sqlite3 as sq

with sq.connect("cars.db") as con:
     cur = con.cursor() # для исполнения запроса - создаете один раз в одном соедение

     cur.execute("""CREATE TABLE IF NOT EXISTS cars (
     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
     model TEXT,
     price INTEGER
     )""")# execute позволяет писать sql запрос
     # НЕЯВНЫЙ ВЫЗОВ con.commit() – применение всех изменений в таблицах БД;
     # con.close() – закрытие соединения с БД.

# Добавлять записи
def add_car(cur, model, price):
     # 2 способа добавить запись в таблицу
     # cur.execute(f"INSERT INTO cars (model, price) VALUES ('{model}', {price})")
     if price < 0:
          print("Цена должна быть >= 0")
          return 1
     cur.execute("INSERT INTO cars (model, price) VALUES (?, ?)", (model, price))


model = "car5"
price = -13400
# Добавлять записи
with sq.connect("cars.db") as con:
     cur = con.cursor()
     add_car(cur, model, price)


# Просмотр записи
def show_car(cur, model=None, price=None):
     condition = ''
     if model is not None:
          condition = 'where model = "' + model + '"'
     if price is not None:
          condition = 'where price = ' + str(price)
     cur.execute(f"SELECT * FROM cars where model = '{model}' and price={price}")
# Редактировать
# Удалять


