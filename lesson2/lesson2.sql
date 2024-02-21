/* Создание таблицы "Студенты":
Создайте таблицу с именем "Students".
Включите столбцы для идентификатора студента, имени, фамилии, возраста и курса.
Установите первичный ключ для столбца идентификатора студента.
Убедитесь, что столбцы имени и фамилии не могут содержать пустые значения.
Добавьте 3 записи
*/
CREATE TABLE IF NOT EXISTS students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	firstName TEXT NOT NULL,
	lastName TEXT NOT NULL,
	age INTEGER DEFAULT 18 CHECK (age > 0),
	course INTEGER
);

-- INSERT INTO students(firstName, lastName) VALUES ("Иван", "Иванов");
/*INSERT INTO students(firstName, lastName, course)
VALUES
("Мария", "Иванова", 1),
("Игорь", "Ломтев", 2);

INSERT INTO students(age, firstName, lastName, course)
VALUES
(20, "Алина", "Лукина", 1)*/
/*INSERT INTO students(age, firstName, lastName, course)
VALUES
(-10, "Алина", "Лукина", 1) */-- запись не может быть добавлена

-- SELECT * from students;


/*------------------------------------------------------------*/
/*

Создание таблицы "Заказы":
Создайте таблицу с именем "Orders".
Включите столбцы для идентификатора заказа, идентификатора клиента, даты заказа и общей суммы.
Установите первичный ключ для столбца идентификатора заказа.
Добавьте 3 записи
*/


CREATE TABLE IF NOT EXISTS orders (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_client INTEGER NOT NULL,
	date_z DATE NOT NULL,
	summ INTEGER CHECK (summ > 0)
);
/*
INSERT INTO orders(id_client, date_z, summ) VALUES ( 7777, "2024-02-21", 1000);
INSERT INTO orders(id_client, date_z, summ) VALUES ( 7747, "2024-01-21", 1500);
INSERT INTO orders(id_client, date_z, summ) VALUES ( 7787, "2023-02-21", 1300);
*/

-- SELECT * FROM orders;
-- SELECT date_z FROM orders;
-- SELECT date_z, summ FROM orders;


/*------------------------------------------------------------*/
SELECT * FROM students;
-- покажи записи о студентах первого курса
SELECT * FROM students WHERE course = 1;
-- покажи всех студентов старше 20 лет
SELECT * FROM students WHERE age >= 20;
-- покажи всех студентов младше 20 лет и учащиеся на 2 курсе
SELECT * FROM students WHERE age < 20 AND course = 2;

-- Покажи студентов с фамилией Иванов(а)
SELECT * FROM students WHERE lastName LIKE "Иванов%";

-- Покажи студентов, у которых нет курса
SELECT * FROM students where course is NULL;

-- Покажи всех студентов кроме тех, у которых нет курса
SELECT * FROM students where course is  NOT NULL;


-- SELECT * FROM students WHERE lastName LIKE 'И[виано]%'; -- ОБЯЗАТЕЛЬНО одинарные кавычки

/*------------------------------------------------------------*/

SELECT * FROM orders;
-- покажи записи заказов выше 1300 и ниже 1500
-- SELECT  * FROM orders where summ>= 1300 AND summ <= 1500;
SELECT * FROM orders WHERE summ BETWEEN 1300 AND 1500;

-- покажи заказы за 2024 год
--SELECT * FROM orders WHERE date_z LIKE "2024-%";
SELECT * FROM orders WHERE strftime('%Y', date_z) = "2024";

-- покажи заказы за 2024 год  за март и февраль
SELECT * FROM orders WHERE strftime('%Y', date_z) = "2024" AND strftime('%m', date_z) BETWEEN "02" AND "03";

/*------------------------------------------------------------*/

CREATE TABLE IF NOT EXISTS  Clients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date DATE DEFAULT CURRENT_DATE,
    email TEXT DEFAULT 'example@example.com',
    phone_number TEXT NOT NULL DEFAULT '000-000-0000'
);
/*
INSERT INTO Clients (name, birth_date, email, phone_number) VALUES
('Иванов Иван', '1990-05-15', 'ivanov@example.com', '123-456-7890'),
('Петров Петр', '1985-08-20', 'petrov@example.com', '987-654-3210'),
('Сидорова Елена', '1995-02-10', 'sidorova@example.com', '111-222-3333'),
('Смирнова Ольга', '1980-11-25', 'smirnova@example.com', '444-555-6666'),
('Козлова Анна', '1975-07-30', 'kozlova@example.com', '777-888-9999'),
('Новиков Александр', '1992-04-05', 'novikov@example.com', '000-111-2222'),
('Морозов Владимир', '1987-09-12', 'morozov@example.com', '333-444-5555'),
('Кузнецова Мария', '1998-03-20', 'kuznetsova@example.com', '666-777-8888'),
('Федоров Дмитрий', '1983-06-18', 'fedorov@example.com', '999-000-1111'),
('Алексеева Наталья', '1979-12-08', 'alekseeva@example.com', '222-333-4444');
*/



/*
Получить список всех клиентов вместе с их именами и номерами телефонов.
Найти клиентов, родившихся после 1990 года.
Получить список клиентов, чьи имена начинаются на букву "А".
Найти клиентов, у которых номер телефона заканчивается на "0".
Получить список клиентов, чьи имена состоят более чем из 10 символов.
Найти клиентов, у которых электронная почта содержит слово "example".

Получить список клиентов, отсортированный по алфавиту по имени.
Найти клиентов, у которых дата рождения совпадает с текущей датой.*/

-- SELECT name, phone_number FROM Clients;
-- SELECT * from Clients WHERE strftime("%Y", birth_date) > "1990";
-- SELECT * FROM Clients WHERE name like "% А%";
-- SELECT * FROM Clients WHERE phone_number like "%0"
-- SELECT * FROM Clients WHERE length(name) > 10;
-- SELECT * FROM Clients WHERE email like "%example%"
-- Получить список клиентов, отсортированный по алфавиту по имени.
SELECT * FROm clients order by name ASC;

-- Найти клиентов, у которых дата рождения совпадает с текущей датой.
SELECT * FROm clients where birth_date = CURRENT_DATE;


 /*ПОСМОТРИМ В ПН*/

-- Получить количество клиентов, родившихся в каждом году.
-- Найти клиентов, чьи имена содержат цифры.