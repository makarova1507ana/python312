import sqlite3

# Декортатор для установки соединения с БД
def db_connection(func):
    """
    Декоратор для установки и закрытия соединения с базой данных.
    """
    def wrapper(self, *args, **kwargs):
        # Устанавливаем соединение с базой данных
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        # Вызываем оборачиваемую функцию
        result = func(self, *args, **kwargs) # create_table| add_book  и т.д.
        # Закрываем соединение с базой данных
        self.connection.commit()
        self.connection.close()
        return result
    return wrapper

'''
BookDatabase будет представлять таблицу книг Books
'''
class BookDatabase:# есть бд books.db и там есть таблица Books
    def __init__(self, db_name='books.db'):
        """
        Инициализация класса BookDatabase.

        Args:
        - db_name (str): Имя файла базы данных SQLite.
        """
        self.db_name = db_name
        self.create_table()  # Создание таблицы при инициализации экземпляра класса

    @db_connection # Декортатор для установки соединения с БД
    def create_table(self):
        """
        Создание таблицы books в базе данных, если она не существует.
        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books
                               (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)''')

    @db_connection
    def add_book(self, title, author, year):
        """
        Добавление новой книги в базу данных.

        Args:
        - title (str): Заголовок книги.
        - author (str): Автор книги.
        - year (int): Год выпуска книги.
        """
        self.cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))

    @db_connection
    def get_books(self):
        """
        Получение списка всех книг из базы данных.

        Returns:
        - list: Список кортежей с информацией о книгах.
        """
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall() # fetchall() -> [(), (), ... ()]

    @db_connection
    def edit_book(self, book_id, title=None, author=None, year=None):
        """
        Редактирование информации о книге по ее идентификатору.

        Args:
        - book_id (int): Идентификатор книги.
        - title (str): Новый заголовок книги (опционально).
        - author (str): Новый автор книги (опционально).
        - year (int): Новый год выпуска книги (опционально).
        """
        update_query = 'UPDATE books SET '
        update_data = [] # update_data = [title, author, author ]

        if title:
            update_query += 'title = ?, ' # update_query = "UPDATE books SET + title = ?, "
            update_data.append(title) #update_data =[] добавли title
        if author:
            update_query += 'author = ?, '
            update_data.append(author)
        if year:
            update_query += 'year = ?, '
            update_data.append(author)

        update_query = update_query.rstrip(', ') # rstrip(', ') -> удалит последнюю запятую и пробел
        update_query += ' WHERE id = ?'
        update_data.append(book_id)

        self.cursor.execute(update_query, tuple(update_data))

    @db_connection
    def delete_book(self, book_id):
        """
        Удаление книги из базы данных по ее идентификатору.

        Args:
        - book_id (int): Идентификатор книги.
        """
        self.cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))

# Пример использования класса BookDatabase
book_db = BookDatabase()

book_db.add_book('1984', 'George Orwell', 1949)
book_db.add_book('To Kill a Mockingbird', 'Harper Lee', 1960)
book_db.add_book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)

print("Список всех книг:")
books = book_db.get_books()
for book in books:
    print(book)

book_db.edit_book(1, title='Animal Farm')
book_db.edit_book(1, author='George Orwell')

print("\nСписок всех книг после редактирования:")
books = book_db.get_books()
for book in books:
    print(book)

book_db.delete_book(2)

print("\nСписок всех книг после удаления:")
books = book_db.get_books()
# print(books)
for book in books:
    print(book)