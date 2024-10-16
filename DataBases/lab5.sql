CREATE DATABASE lab5;

 CREATE TABLE  customers (
     customer_id INT,
     customer_name VARCHAR(255),
     city VARCHAR(255),
     grade INT,
     salesman_id INT
 );

INSERT INTO customers (customer_id, customer_name, city, grade, salesman_id)
VALUES (3002, 'Nick Rimando', 'New York', 100, 5001),
       (3005, 'Graham Zusi', 'California', 200, 5002),
       (3004, 'Fabian Johns', 'Paris', 300, 5006),
       (3007, 'Brad Davis', 'New York', 200, 5001),
       (3009, 'Geoff Camero', 'Berlin', 100, 5003),
       (3008, 'Julian Green', 'London', 300, 5002);

insert into customers(customer_id, customer_name, city, salesman_id)
values (3001, 'Brad Guzan', 'London', 5005);


 CREATE TABLE  orders (
     ord_no INT,
     purchase_amt FLOAT,
     ord_date DATE,
     customer_id INT,
     salesman_id INT
 );

INSERT INTO orders (ord_no, purchase_amt, ord_date, customer_id, salesman_id)
VALUES (70001, 150.5, '2012-10-05', 3005, 5002),
       (70009, 270.65, '2012-09-10', 3001, 5005),
       (70002, 65.26, '2012-10-05', 3002, 5001),
       (70004, 110.5, '2012-08-17', 3009, 5003),
       (70007, 948.5, '2012-09-10', 3005, 5002),
       (70005, 2400.6, '2012-07-27', 3007, 5001),
       (70008, 5760, '2012-09-10', 3002, 5001);



SELECT SUM(purchase_amt) FROM orders;

SELECT AVG(purchase_amt) FROM orders;

SELECT COUNT(customer_name) FROM customers;

SELECT MIN(purchase_amt) FROM orders;

SELECT * FROM customers
WHERE customer_name LIKE '%b';

SELECT ord_no from orders join customers on orders.customer_id = customers.customer_id
where city = 'New York';

SELECT * FROM customers JOIN orders ON orders.customer_id = customers.customer_id
WHERE purchase_amt > 10;

SELECT SUM(grade) FROM customers;

SELECT DISTINCT customer_name FROM customers GROUP BY customer_name;

SELECT MAX(grade) FROM customers;





