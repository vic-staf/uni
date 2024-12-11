CREATE DATABASE lab10;


CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL
);


CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    book_id INT REFERENCES Books(book_id),
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    quantity INT NOT NULL
);


CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

INSERT INTO Books (book_id, title, author, price, quantity)
VALUES
    (1, 'Database 101', 'A. Smith', 40.00, 10),
    (2, 'Learn SQL', 'B. Johnson', 35.00, 15),
    (3, 'Advanced DB', 'C. Lee', 50.00, 5);


INSERT INTO Customers (customer_id, name, email)
VALUES
    (101, 'John Doe', 'johndoe@example.com'),
    (102, 'Jane Doe', 'janedoe@example.com');



-- 1
BEGIN;

INSERT INTO Orders (order_id, book_id, customer_id, order_date, quantity)
VALUES (1, 1, 101, CURRENT_DATE, 2);

UPDATE Books
SET quantity = quantity - 2
WHERE book_id = 1;

COMMIT;

---2


-- BEGIN;
--
-- SAVEPOINT savepoint1;
--
-- INSERT INTO Orders (order_id, book_id, customer_id, order_date, quantity)
-- VALUES (2, 3, 102, CURRENT_DATE, 10);
--
-- IF (SELECT quantity FROM Books WHERE book_id = 3) < 10 THEN ROLLBACK TO savepoint1;
-- END IF;
--
-- UPDATE Books
-- SET quantity = quantity - 10
-- WHERE book_id = 3;
--
-- COMMIT;


BEGIN;

SAVEPOINT savepoint1;

DO $$
BEGIN
    IF (SELECT quantity FROM Books WHERE book_id = 3) < 10 THEN ROLLBACK TO savepoint1;
    ELSE
        INSERT INTO Orders (order_id, book_id, customer_id, order_date, quantity)
        VALUES (2, 3, 102, CURRENT_DATE, 10);

        UPDATE Books
        SET quantity = quantity - 10
        WHERE book_id = 3;
    END IF;

END;
$$ LANGUAGE plpgsql;

COMMIT;

---3

BEGIN TRANSACTION ISOLATION LEVEL READ COMMITTED;
UPDATE Books
SET price = price + 5
WHERE book_id = 1;


SELECT price FROM Books WHERE book_id = 1;
COMMIT;

--4
BEGIN;

UPDATE Customers
SET email = 'email@gmail.com'
WHERE customer_id = 101;

COMMIT;




