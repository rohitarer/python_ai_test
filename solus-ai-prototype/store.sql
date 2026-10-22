SELECT current_database(), current_user;

CREATE TABLE employees(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18)
);

INSERT INTO employees (id, name, email, age) VALUES 
(101, 'Rohit', 'rohit@gmail.com', 25),
(102, 'Alice', 'alice@gmail.com', 26);


SELECT * FROM employees;

SELECT name, email FROM employees;

SELECT name, email FROM employees 
WHERE (age>=26);


UPDATE employees
Set age = 28
WHERE id = 102;

SELECT * FROM employees;

DELETE FROM employees
WHERE id = 101;

SELECT * FROM employees;


CREATE TABLE students(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age>=18)
);

SELECT * FROM students;

INSERT INTO students (id, name, age) VALUES
(1, 'Rohit', 19),
(2, 'Alice', 22),
(3, 'Sam', 25);

SELECT * FROM students
WHERE (id=1);


SELECT * FROM students
ORDER BY age ASC;

SELECT * FROM students
ORDER BY age DESC;

-- SELECT * FROM students
-- ORDER BY age DESC
-- LIMIT 2;

INSERT INTO students (id, name, age) VALUES
(4, 'Max', 19);

SELECT DISTINCT age
FROM students;


SELECT * FROM students
WHERE age != 22
ORDER BY age DESC
LIMIT 2;

SELECT * FROM students;

SELECT * FROM students
WHERE age >= 20 AND age <25;

SELECT * FROM students
WHERE age <= 18 OR age >= 29;

SELECT * FROM students
WHERE age IN (18, 25);

SELECT * FROM students
WHERE age BETWEEN 18 AND 25;

SELECT * FROM students
WHERE name LIKE 'R%';

SELECT * FROM students
WHERE name LIKE '%e';

SELECT * FROM students
WHERE name LIKE '%oh%';


SELECT * FROM students
WHERE name LIKE '%ic%';


SELECT * FROM students
WHERE age BETWEEN 20 AND 25;

SELECT * FROM students
WHERE age = 19 OR age = 25;

SELECT * FROM students
WHERE name LIKE 'R%';

SELECT COUNT(*) FROM students;

SELECT COUNT(*) FROM students
WHERE age >= 20;

SELECT SUM(age) FROM students;

SELECT AVG(age) FROM students;

SELECT MIN(age) FROM students;

SELECT MAX(age) FROM students;

ALTER TABLE students
ADD COLUMN departments VARCHAR(100);

SELECT * FROM students;

UPDATE students
SET departments='IT'
WHERE id IN (1,3);

UPDATE students
SET departments = 'HR'
WHERE id IN (2, 4);


SELECT departments, COUNT(*)
FROM departments
GROUP BY departments;


SELECT departments, AVG(age)
FROM students
GROUP BY departments;


SELECT departments, COUNT(*)
FROM students
GROUP BY departments
HAVING COUNT(*)>1;


SELECT departments, AVG(age)
FROM students
GROUP BY departments
HAVING AVG(age) >21;

SELECT departments, COUNT(*)
FROM students
WHERE age >=21
GROUP BY departments
HAVING COUNT(*)>=1;


SELECT departments, AVG(age)
FROM students
GROUP BY departments
HAVING AVG(age)>21;


SELECT * FROM students;

CREATE TABLE departments(
    id INT UNIQUE,
    department_name VARCHAR(100) NOT NULL
);

INSERT INTO departments (id, department_name) VALUES
(10, 'IT'),
(20, 'HR');

SELECT * FROM departments;

ALTER TABLE students
ADD COLUMN department_id INT;

SELECT * FROM students;

UPDATE students
SET department_id = 10
WHERE departments = 'IT';

UPDATE students
SET department_id = 20
WHERE departments = 'HR';

ALTER TABLE students
DROP COLUMN departments;

ALTER TABLE students
Add CONSTRAINT fk_departmentid
FOREIGN KEY (department_id)
REFERENCES departments(id);


SELECT s.name, d.department_name
FROM students s
INNER JOIN departments d
ON s.department_id = d.id;

SELECT * FROM students;

SELECT * FROM students
WHERE age > (
    SELECT AVG(age) FROM students
);

SELECT * FROM students
WHERE age = (
    SELECT MAX(age) FROM students
);

SELECT * FROM employees;

UPDATE employees
SET email = CASE
    WHEN id = 1 THEN 'r@g.c'
    WHEN id = 2 THEN 'a@g.c'
    WHEN id = 3 THEN 's@g.c'
END
WHERE id IN (1, 2, 3);

SELECT * FROM departments;


INSERT INTO departments 
(id, department_name) VALUES
(30, 'Sales'),
(40, 'Director');

ALTER TABLE employees
ADD COLUMN dept_id INT;

UPDATE employees
SET dept_id = CASE
    WHEN id = 102 THEN 40
    WHEN id = 1 THEN 10
    WHEN id = 2 THEN 20
    WHEN id = 3 THEN 30
END 
WHERE id IN (102, 1, 2, 3);


BEGIN;

UPDATE employees
SET dept_id = 40
WHERE id = 102;

UPDATE departments
SET department_name = 'Development'
WHERE id = 20;

SELECT * FROM employees;

SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.id;

COMMIT;


ROLLBACK;


SELECT * FROM employees;

SELECT * FROM departments;

CREATE VIEW employee_details AS
SELECT e.name, e.age, d.department_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.id;


SELECT * FROM employee_details;

UPDATE employees
SET dept_id = 50
WHERE id = 3;

SELECT * FROM employees;

SELECT * FROM departments;