SELECT current_database(), CURRENT_USER;

CREATE TABLE tickets(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date VARCHAR(100) NOT NULL,
    city_name VARCHAR(100) NOT NULL
);


INSERT INTO tickets (id, name, email, date, city_name) VALUES
(1, 'Rohit', 'r@g.c', '1-6-26', 'Belagavi'),
(2, 'Alice', 'a@g.c', '2-2-26', 'Dharwad'),
(3, 'Clara', 'c@g.c', '23-4-26', 'Hubli'),
(4, 'Ganesh', 'g@g.c', '12-3-26', 'Bengaluru');

SELECT * FROM tickets;

ALTER TABLE tickets
ADD COLUMN ticket_id INT,
ADD COLUMN price INT;


UPDATE tickets
SET ticket_id = CASE
    WHEN city_name = 'Belagavi' THEN 10
    WHEN city_name = 'Dharwad' THEN 20
    WHEN city_name = 'Hubli' THEN 30
    WHEN city_name = 'Bengaluru' THEN 40
END
WHERE city_name IN ('Belagavi', 'Dharwad', 'Hubli', 'Bengaluru');

UPDATE tickets
SET price = CASE
    WHEN city_name = 'Belagavi' THEN 150
    WHEN city_name = 'Dharwad' THEN 70
    WHEN city_name = 'Hubli' THEN 80
    WHEN city_name = 'Bengaluru' THEN 600
END
WHERE city_name IN ('Belagavi', 'Dharwad', 'Hubli', 'Bengaluru');

CREATE TABLE cities(
    id INT PRIMARY KEY,
    city_name VARCHAR(100) NOT NULL
);

INSERT INTO cities (id, city_name) VALUES
(10, 'Belagavi'),
(20, 'Dharwad'),
(30, 'Hubli'),
(40, 'Bengaluru');

SELECT * FROM cities;

ALTER TABLE tickets
DROP COLUMN city_name;

ALTER TABLE tickets
ADD CONSTRAINT city_fk
FOREIGN KEY (ticket_id)
REFERENCES cities(id);

SELECT * FROM tickets;


SELECT t.name, t.price, c.city_name
FROM tickets t
INNER JOIN cities c
ON t.ticket_id = c.id;


ALTER TABLE tickets
RENAME ticket_id TO cities_id;

UPDATE tickets
SET cities_id = NULL
WHERE id = 3;


SELECT t.name, t.date, c.city_name, t.price
FROM tickets t
LEFT JOIN cities c
ON t.cities_id = c.id;


INSERT INTO cities(id, city_name) VALUES
(50, 'Mysore');

SELECT * FROM cities;

SELECT t.name, c.city_name
FROM tickets t
RIGHT JOIN cities c
ON t.cities_id = c.id;

SELECT t.name, c.city_name
FROM cities c
Left JOIN tickets t
ON c.id = t.cities_id;


SELECT t.name, c.city_name
FROM tickets t
FULL OUTER JOIN cities c
ON t.cities_id = c.id;


SELECT t.name AS traveller,
c.name AS city_friend
FROM tickets t
LEFT JOIN tickets c
ON t.cities_id = c.cities_id;


SELECT * FROM  tickets
WHERE cities_id IN (
    SELECT id FROM cities
    WHERE city_name IN ('Belagavi', 'Dharwad')
);


SELECT * FROM cities c
WHERE EXISTS(
    SELECT 1 
    FROM tickets t
    WHERE c.id = t.cities_id
);

 

CREATE TABLE products(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INT CHECK (price > 0) NOT NULL
);

INSERT INTO products 
(name, price) VALUES
('Rohit', 100),
('Sam', 200),
('Alice', 300);

SELECT * FROM products;
