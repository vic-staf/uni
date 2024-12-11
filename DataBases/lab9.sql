CREATE DATABASE lab9;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary INTEGER NOT NULL
);


INSERT INTO employees (name, salary) VALUES
('Alice Johnson', 55000),
('Bob Smith', 48000),
('Carol Davis', 62000),
('David Wilson', 53000),
('Emma Brown', 70000),
('Frank Taylor', 45000);


-- 1
CREATE OR REPLACE FUNCTION increase_value(val INTEGER)
RETURNS INTEGER AS $$
BEGIN
    RETURN val + 10;
END;
$$ LANGUAGE plpgsql;

SELECT increase_value(2);

-- 2
CREATE OR REPLACE FUNCTION compare_numbers(num1 INTEGER, num2 INTEGER)
RETURNS TEXT AS $$
BEGIN
    IF num1 > num2 THEN RETURN 'num1 greater';
    ELSIF num1 < num2 THEN RETURN 'num1 less';
    ELSE RETURN 'equal';
    END IF;
END;
$$ LANGUAGE plpgsql;

select compare_numbers(10, 8);

-- 3
CREATE OR REPLACE FUNCTION number_series(n INTEGER)
RETURNS TEXT AS $$
DECLARE
    result TEXT := '';
    i INTEGER := 1;
BEGIN
    FOR i IN 1..n LOOP
    result := result || i || ' ';
    END LOOP;

    RETURN(result);
END;

$$ LANGUAGE plpgsql;

SELECT number_series(6);

-- 4
CREATE OR REPLACE FUNCTION find_employee(name_emp TEXT)
RETURNS SETOF employees AS $$
BEGIN
        RETURN QUERY(SELECT * FROM employees
        WHERE name = name_emp);

END;
$$ LANGUAGE plpgsql;

SELECT * FROM find_employee('Alice Johnson');

-- 5
CREATE OR REPLACE FUNCTION list_products(category_product TEXT)
RETURNS SETOF products AS $$
BEGIN
    RETURN QUERY (SELECT * FROM products
                 WHERE category = category_product);
END;
$$ LANGUAGE plpgsql;

-- 6
CREATE OR REPLACE FUNCTION calculate_bonus(salary INTEGER, percentage NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
    RETURN salary * (percentage / 100);
END;
$$ LANGUAGE plpgsql;

SELECT calculate_bonus(200, 5.0);

CREATE OR REPLACE FUNCTION update_salary(emp_id INTEGER, percentage NUMERIC)
RETURNS VOID AS $$
DECLARE
    bonus NUMERIC;
BEGIN
    SELECT calculate_bonus(salary, percentage) INTO bonus
    FROM employees
    WHERE emp_id = id;

    UPDATE employees
    SET salary = salary + bonus
    WHERE emp_id = id;


END;
$$ LANGUAGE plpgsql;

SELECT update_salary(1, 50.0);


DROP TABLE employees CASCADE;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary INTEGER NOT NULL,
    attendance INTEGER NOT NULL,
    department VARCHAR(100) NOT NULL
);


INSERT INTO employees (name, salary, attendance, department) VALUES
('Alice Johnson', 55000, 5, 'IT'),
('Bob Smith', 48000, 10, 'IT'),
('Carol Davis', 62000, 14, 'Marketing'),
('David Wilson', 53000, 2, 'Marketing'),
('Emma Brown', 70000, 8, 'IT'),
('Frank Taylor', 45000, 1, 'Sales');


-- 7
CREATE OR REPLACE FUNCTION complex_calculation(id_emp INTEGER, dep_emp TEXT)
RETURNS TEXT AS $$
DECLARE
    integer_result INTEGER;
    string_result TEXT;
BEGIN

    DECLARE
        s INTEGER;
        a INTEGER;
    BEGIN
        SELECT salary INTO s FROM employees
        WHERE id = id_emp;

        SELECT attendance INTO a FROM employees
        WHERE id = id_emp;

        integer_result := s * a;
    END;


    DECLARE
        n TEXT;
    BEGIN
        SELECT name INTO n FROM employees
        WHERE id = id_emp;

        string_result := n || ' in the department ' || dep_emp;
    END;


    RETURN string_result || ' has overall points: ' || integer_result;

END;
$$ LANGUAGE plpgsql;

SELECT complex_calculation(5, 'IT');

