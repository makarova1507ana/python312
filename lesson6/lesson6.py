import sqlite3 as sq

with sq.connect("cars.db") as con:
     cur = con.cursor() # для исполнения запроса - создаете один раз в одном соедение

     cur.execute("""CREATE TABLE IF NOT EXISTS cars (
     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
     model TEXT,
     price INTEGER CHECK(price >= 0),
     photo BLOB
     )""")# execute позволяет писать sql запрос
     # НЕЯВНЫЙ ВЫЗОВ con.commit() – применение всех изменений в таблицах БД;
     # con.close() – закрытие соединения с БД.

# Добавлять записи
def add_car(cur, model, price, photo_path):
     # 2 способа добавить запись в таблицу
     # cur.execute(f"INSERT INTO cars (model, price) VALUES ('{model}', {price})")
     if price < 0:
          print("Цена должна быть >= 0")
          return 1
     # сохрание бинарных даныных BLOB (медиа)
     # бинарные формат -> 10101

     # считать изображение бинарном формате
     with open(photo_path , "rb") as f:
          photo = f.read() #binary format
          #print(photo)

     # ->  BLOB
     binary_photo = sq.Binary(photo)
     cur.execute("INSERT INTO cars (model, price, photo) VALUES (?, ?, ?)", (model, price, binary_photo))


model = "car6"
price = 13400
photo_path = "car2.jpg"
# Добавлять записи
with sq.connect("cars.db") as con:
     cur = con.cursor()
     add_car(cur, model, price, photo_path=photo_path)


# Просмотр записи
def show_car(cur, model=None, price=None):
     condition = 'where true'
     if model is not None:
          condition += ' AND model = "' + model + '"'
     if price is not None:
          condition += ' AND price = ' + str(price)
     rows = cur.execute(f"SELECT * FROM cars {condition}")
     for row in rows:
          print(row)

# with sq.connect("cars.db") as con:
#      cur = con.cursor()
#      show_car(cur)

# Редактировать
def edit_car(cur, id=None, model=None, price=None):
     condition = 'where true  '
     if id is not None:
          condition += f' and car_id = {id}'
     if model is not None:
          cur.execute(f"""UPDATE cars
                         SET model = '{model}'
                        {condition}""")
     if price is not None:
          cur.execute(f"""UPDATE cars
                              SET price = {price}
                              {condition}""")
with sq.connect("cars.db") as con:
     cur = con.cursor()
     edit_car(cur,  model = '000car000', price="321")
     edit_car(cur, 3, model='111car111', price="111111")
     show_car(cur)
# Удалять


# бэкап - .db -> .sql(в котором есть запросы на создание всех таблиц и вставку данных в эту таблицу)

with sq.connect("cars.db") as con:
     cur = con.cursor()
     with open("cars_copy.sql","w") as f:
          for sql in con.iterdump():
               f.write('\n'+sql)




# интерфейс
# ORM -> Object–relational mapping
# таблица -> класса, который будет  взаимодействовать  с БД(с данной таблицей)