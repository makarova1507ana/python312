CREATE TABLE IF NOT EXISTS Users
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS PhoneNumbers
(
  id INTEGER  PRIMARY KEY  AUTOINCREMENT,
  number INTEGER NOT NULL CHECK (number > 100000),
  id_user INTEGER,
  FOREIGN KEY (id_user) REFERENCES Users(id)
);
/*
INSERT INTO Users(name)
VALUES ("Petya"),
("Vasya"),
("Ivan"),
("Margo");
INSERT INTO PhoneNumbers(number, id_user)
VALUES (111111, 1),
(222222,1),
(333333,2),
(555555,NULL),
(444444,3);*/
