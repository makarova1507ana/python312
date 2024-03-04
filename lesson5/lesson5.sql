
-- Создаем таблицу departments
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

-- Создаем таблицу employees с внешним ключом department_id
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department_id INTEGER,
    position TEXT,
    salary REAL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
-- Создаем таблицу проектов
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    description TEXT
);

-- Создаем таблицу задач
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    name TEXT,
    description TEXT,
    status TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Создаем таблицу, связывающую сотрудников с задачами
CREATE TABLE IF NOT EXISTS employee_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    task_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);

/*
-- Вставляем данные в таблицу departments
INSERT INTO departments (name) VALUES ('HR'),
('IT'),
('Finance'),
('Menegment');

-- Вставляем данные в таблицу employees
INSERT INTO employees (name, department_id, position, salary) VALUES 
('John Doe', 1, 'HR Manager', 5000),
('John White', 1, 'HR Assistant', 4500),
('Jane Smith', 1, 'HR Assistant', 3500),
('Mike Johnson', 2, 'Software Engineer', 6000),
('Emily Brown', 2, 'Database Administrator', 5500),
('David Wilson', 3, 'Financial Analyst', 5200);

-- Вставляем данные в таблицу projects
INSERT INTO projects (name, description) VALUES ('Project A', 'Description for Project A');
INSERT INTO projects (name, description) VALUES ('Project B', 'Description for Project B');
INSERT INTO projects (name, description) VALUES ('Project C', 'Description for Project C');

-- Вставляем данные в таблицу tasks
INSERT INTO tasks (project_id, name, description, status) VALUES (1, 'Task 1 for Project A', 'Description for Task 1', 'In Progress');
INSERT INTO tasks (project_id, name, description, status) VALUES (1, 'Task 2 for Project A', 'Description for Task 2', 'New');
INSERT INTO tasks (project_id, name, description, status) VALUES (2, 'Task 1 for Project B', 'Description for Task 1', 'Completed');
INSERT INTO tasks (project_id, name, description, status) VALUES (3, 'Task 1 for Project C', 'Description for Task 1', 'In Progress');
INSERT INTO tasks (project_id, name, description, status) VALUES (2, 'Task 2 for Project B', 'Description for Task 2', 'Is opened');

-- Вставляем данные в таблицу employee_tasks
INSERT INTO employee_tasks (employee_id, task_id) VALUES (1, 1);
INSERT INTO employee_tasks (employee_id, task_id) VALUES (1, 2);
INSERT INTO employee_tasks (employee_id, task_id) VALUES (2, 3);
INSERT INTO employee_tasks (employee_id, task_id) VALUES (3, 4);*/



--3 Получить список всех cотрудников, у которых еще не назначены задачи.
/*select tasks.id, tasks.name, tasks.status, employee_id, task_id, employees.id, employees.name
from tasks
 left join employee_tasks  ON task_id = tasks.id -- employee_tasks - связывает tasks и employees
  left join employees on employee_id = employees.id;
  */



  --Получить список всех задач, которые еще не назначены на сотрудников.
/*select employees.id, employees.name -- для проверки можно использовать tasks.id, tasks.name, tasks.status, employee_id, task_id,
from employees
 left join employee_tasks  ON employee_id = employees.id -- employee_tasks - связывает tasks и employees
  left join tasks on task_id = tasks.id
  where task_id is NUll; */


-- Получить список всех сотрудников и количество задач, назначенных каждому из них.
/*select COUNT(*) as "кол-во задач",  employees.id, employees.name
from tasks
join employee_tasks  ON task_id = tasks.id -- employee_tasks - связывает tasks и employees
join employees on employee_id = employees.id
GROUP by employee_id;*/
/*
-- 6 Получить список всех сотрудников и количество задач, назначенных каждому из них.
select COUNT(*) as "кол-во задач",  employee_id, name
from  employee_tasks  JOIN employees on employee_id = employees.id
GROUP by employee_id;

-- 2 Получить список всех задач, назначенных определенному сотруднику.

SELECT employees.id as 'name_id', employees.name, tasks.id as 'task_id', tasks.name FROM tasks
JOIN employee_tasks on task_id = tasks.id
JOIN employees ON employee_id = employees.id;


-- 4 Получить общее количество задач в каждом проекте.
SELECT COUNT(*) as 'кол-во задач', * from tasks
GROUP BY project_id;

-- 5 Получить список всех задач, статус которых "In Progress".
SELECT * FROM tasks WHERE status = "In Progress";

-- 7 Получить список всех задач для конкретного проекта с описанием проекта.
SELECT tasks.id, project_id, tasks.name, tasks.description, projects.name, projects.description FROM tasks
JOIN projects
ON project_id = projects.id;


-- 1 Получить все задачи для конкретного проекта.
select * FROM tasks
JOIN projects ON projects.id = project_id ;--ПК(проектов) =ФК(проекта у задачи)



-- 8 Получить список всех сотрудников, назначенных на задачи в проекте.
SELECT project_id, projects.name, employees.name FROM tasks
JOIN projects ON project_id = projects.id
JOIN employee_tasks ON task_id = tasks.id
JOIN employees ON employee_id = employees.id;



-- 9 Получить список всех задач, отсортированных по статусу и имени проекта.
SELECT * FROM tasks
JOIN projects ON project_id = projects.id
ORDER BY status, projects.name ;



-- 10. Получить общее количество задач, завершенных в каждом проекте.
SELECT projects.name, COUNT(tasks.id) AS completed_tasks
FROM projects
LEFT JOIN tasks ON projects.id = tasks.project_id
WHERE tasks.status = 'Completed'
GROUP BY projects.name;

*/



--Получить список всех задач, назначенных определенному сотруднику.
SELECT * from employees
left join employee_tasks ON employee_id = employees.id
left JOIN tasks ON task_id = tasks.id
WHERE employees.name = "John Doe";--"Emily Brown" ;