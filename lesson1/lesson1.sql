-- однострочный комментарий
/*многострочный комментарий*/

-- таблиц ИГР
create TABLE IF NOT EXISTS games (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	score INTEGER
);
INSERT INTO GAMES (score) VALUES (120); -- вставить данные в тбалицу

SELECT * FROM GAMES; -- получить данные из таблицы
