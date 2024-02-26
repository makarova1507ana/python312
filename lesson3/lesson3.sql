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
-- SELECT * FROm clients order by name ASC;

-- Найти клиентов, у которых дата рождения совпадает с текущей датой.
-- SELECT * FROm clients where birth_date = CURRENT_DATE;


 /*Посмотрели В ПН*/
-- пример
-- SELECT COUNT(id) FROM Clients where strftime("%Y", birth_date) > "1980";

-- Получить количество клиентов, родившихся в каждом году.

-- INSERT INTO Clients (name, birth_date, email, phone_number) VALUES ('Иванов Иван', '1980-05-15', 'ivanovivan@example.com', '123-556-7890');
-- SELECT COUNT(id),  birth_date FROM Clients Group BY  strftime("%Y", birth_date);

-- Найти клиентов, чьи имена содержат цифры.
-- INSERT INTO Clients (name, birth_date, email, phone_number) VALUES ('Иванов 2Иван', '1990-05-15', 'ivanovivan2@example.com', '103-556-7890');
-- SELECT name from  clients WHERE name REGEXP '[0-9]';



CREATE TABLE IF NOT EXISTS orders (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	date_z DATE NOT NULL,
	summ INTEGER CHECK (summ > 0)
);
/*
INSERT INTO orders(date_z, summ) VALUES ( "2024-02-21", 1000);
INSERT INTO orders(date_z, summ) VALUES ("2024-01-21", 1500);
INSERT INTO orders(date_z, summ) VALUES ( "2023-02-21", 1300);

INSERT INTO orders(date_z, summ) VALUES ( "2024-02-28", 1500);
INSERT INTO orders(date_z, summ) VALUES ( "2023-01-21", 1301);
INSERT INTO orders(date_z, summ) VALUES ( "2022-02-20", 1302);
INSERT INTO orders(date_z, summ) VALUES ( "2023-03-19", 19000);
*/


-- SELECT * from orders;
/*  -----------------Агрегатные функции--------------------- */
-- COUNT, SUM, AVG - среднее знач., MIN, MAX
/*--примеры для данных функции с COUNT-- (но работает так со всеми)*/

-- общее кол-во заказов
-- SELECT COUNT(id) as "кол-во заказов" from orders;

-- кол-во заказов на сумму более 10000;
/*SELECT COUNT(id)as "кол-во заказов"
from orders
where summ>10000;
*/


-- кол-во заказов за каждый год в таблице
/*SELECT COUNT(id) as "count", strftime("%Y", date_z) as "year"
from orders
GROUP BY  strftime("%Y", date_z);
*/

-- кол-во заказов за год 2024 за каждый месяц в таблице
/*SELECT COUNT(id) as "count", strftime("%m", date_z) as "2024 месяц"
from orders
WHERE strftime("%Y", date_z)= "2024"
GROUP BY strftime("%m", date_z);
*/

/*------------------HAVING---------------------*/
-- Посчитать общую сумму заказов за 2023 год
/*SELECT SUM(summ) as "sum"
from orders
where strftime("%Y", date_z) = "2023"; */


-- Посчитать общую сумму заказов за каждый год,
-- показать такую общую сумму, если она больше 5000
/*SELECT SUM(summ) as "sum" , strftime("%Y", date_z) as "year"
from orders
GROUP BY strftime("%Y", date_z)
HAVING SUM(summ) > 500;*/


-- Посчитать общую сумму заказов за 2023 год,
-- показать такую общую сумму, если она больше 20000
/*SELECT SUM(summ) as "sum" , strftime("%Y", date_z) as "year"
from orders
where strftime("%Y", date_z) = "2023"
GROUP BY strftime("%Y", date_z)
HAVING SUM(summ) > 20000;*/




CREATE TABLE IF NOT EXISTS Projects (
    id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    start_date DATE DEFAULT CURRENT_DATE,
    end_date DATE DEFAULT NULL,
    status TEXT DEFAULT 'В процессе'
);
/*
INSERT INTO Projects (project_name, start_date, end_date, status) VALUES
('Project1', '2023-01-01', '2023-02-01', 'Завершен'),
('Project2', '2023-02-01', '2023-03-01', 'В процессе'),
('Project3', '2023-03-01', NULL, 'В процессе'),
('Project4', '2023-04-01', 2023-08-01, 'Завершен'),
('Project5', '2023-05-01', NULL, 'В процессе'),
('Project6', '2023-06-01', NULL, 'В процессе'),
('Project7', '2023-07-01', NULL, 'В процессе'),
('Project8', '2023-08-01', 2023-08-02, 'Завершен'),
('Project9', '2023-09-01', NULL, 'В процессе'),
('Project10', '2023-10-01', NULL, 'В процессе');
*/
/*
-- 1. Получить количество всех проектов со статусом 'В процессе':
SELECT COUNT(*) -- COUNT(*) считает кол-во записей в строках
FROM Projects
WHERE status = 'В процессе';

-- 2. Получить количество всех проектов каждого статуса:
SELECT status, COUNT(*)
FROM Projects
GROUP BY status;


-- 3. Получить количество всех проектов, у которых не задана дата окончания:

SELECT COUNT(*)
FROM Projects
WHERE end_date IS NULL;


-- 4. Получить количество проектов, начавшихся после 2023-04-01:
SELECT COUNT(*)
FROM Projects
WHERE start_date > '2023-04-01';
*/

-- 5. Рассчитать среднее время выполнения проекта:

SELECT end_date, avg (JulianDay(end_date) - JulianDay(start_date)) as "средне кол-во дней"
FROM Projects
WHERE end_date is not null; -- !!! НО берет всякую еренду


-- SELECT AVG(ABS(JulianDay("2024-01-01") - JulianDay("2024-01-02")))
-- FROM Projects

/* ----СВЯЗЬ ОДИН ко МНОГИМ----*/
CREATE TABLE IF NOT EXISTS CLIENTS (
 ID INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT DEFAULT "NO NAME"
);

CREATE TABLE IF NOT EXISTS phones (
 ID INTEGER PRIMARY KEY AUTOINCREMENT,
 phone_number INTEGER NOT NULL,
 id_client INTEGER,
 FOREIGN KEY (id_client) REFERENCES CLIENTS(ID)
 );
 /*
INSERT INTO CLIENTS(name)
VALUES ("Petya"),
("Vasya"),
("Ivan"),
("Margo");
INSERT INTO phones(phone_number, id_client)
VALUES (111, 1),
(222,1),
(333,2),
(444,3);*/

SELECT * FROM clients, phones
where
CLIENTS.ID = Phones.id_client; -- ПК (primary key) = ФК (foreign key)
