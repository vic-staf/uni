CREATE DATABASE lab8;

CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    commission DECIMAL(3, 2)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(50),
    city VARCHAR(50),
    grade INT,
    salesman_id INT REFERENCES salesman(salesman_id)
);

CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 3),
    ord_date DATE,
    customer_id INT REFERENCES customers(customer_id),
    salesman_id INT REFERENCES salesman(salesman_id)
);

INSERT INTO salesman VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lauson Hen', 'Rome', 0.12),
(5007, 'Paul Adam', 'Rome', 0.13);


INSERT INTO customers VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', 100, 5005),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Geoff Camero', 'Berlin', 100, 5003),
(3009, 'Julian Green', 'London', 300, 5005);


INSERT INTO orders VALUES
(70001, 150.5, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26, '2012-10-05', 3002, 5001),
(70004, 110.5, '2012-08-17', 3009, 5005),
(70007, 948.5, '2012-09-10', 3005, 5002),
(70005, 2400.6, '2012-07-27', 3007, 5003),
(70008, 5760, '2012-09-10', 3002, 5001);



--- 3
CREATE ROLE junior_dev WITH LOGIN PASSWORD 'password123';

---4
CREATE VIEW ny_salesmen AS
SELECT * FROM salesman
WHERE city = 'New York';

---5
CREATE VIEW order_details AS
SELECT
    o.ord_no,
    c.cust_name AS customer_name,
    s.name AS salesman_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN salesman s ON o.salesman_id = s.salesman_id;

GRANT ALL PRIVILEGES ON TABLE order_details TO junior_dev;

---6
CREATE VIEW top_customers AS
SELECT * FROM customers
WHERE grade = (SELECT MAX(grade) FROM customers);

GRANT SELECT ON TABLE top_customers TO junior_dev;

---7
CREATE VIEW salesman_count_by_city AS
SELECT city, COUNT(*) AS total_salesmen
FROM salesman
GROUP BY city;

---8
CREATE VIEW salesmen_with_multiple_customers AS
SELECT s.salesman_id, s.name, COUNT(c.customer_id) AS total_customers
FROM salesman s
JOIN customers c ON s.salesman_id = c.salesman_id
GROUP BY s.salesman_id, s.name
HAVING COUNT(c.customer_id) > 1;

---9
CREATE ROLE intern;
GRANT junior_dev TO intern;



