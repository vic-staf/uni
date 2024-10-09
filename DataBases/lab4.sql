CREATE DATABASE lab4;

CREATE TABLE Warehouses (
    code INTEGER NOT NULL,
    location VARCHAR (255),
    capacity INTEGER NOT NULL
);

INSERT INTO Warehouses(code, location, capacity) VALUES
        (1, 'Chicago', 3),
        (2, 'Chicago', 4),
        (3, 'New York', 7),
        (4, 'Los Angeles', 2),
        (5, 'San Francisco', 8);

CREATE TABLE Boxes (
    code CHAR (4),
    contents VARCHAR (255),
    value REAL,
    warehouse INTEGER
);

INSERT INTO Boxes(code, contents, value, warehouse) VALUES
        ('0MN7', 'Rocks', 180, 3),
        ('4H8P', 'Rocks', 250, 1),
        ('4RT3', 'Scissors', 190, 4),
        ('7G3H', 'Rocks', 200, 1),
        ('8JN6', 'Papers', 75, 1),
        ('8Y6U', 'Papers',50, 3),
        ('9J6F', 'Papers', 175, 2),
        ('LL08', 'Rocks', 140, 4),
        ('P0H6', 'Scissors', 125, 1),
        ('P2T6', 'Scissors', 150, 2),
        ('TU55', 'Papers', 90, 5);

SELECT * FROM warehouses;

SELECT * FROM boxes WHERE value > 150;

SELECT DISTINCT contents FROM boxes;

SELECT warehouse, COUNT(*) AS number
FROM boxes
GROUP BY warehouse;

SELECT warehouse, COUNT(*) AS number
FROM boxes
GROUP BY warehouse
HAVING COUNT(*) >2;

INSERT INTO warehouses (code,location,capacity) VALUES
            (6, 'New York', 3);

INSERT INTO Boxes(code, contents, value, warehouse) VALUES
        ('H5RT', 'Papers', 200, 2);




UPDATE boxes
SET value = 0.85 * value
WHERE value = (SELECT value FROM boxes ORDER BY value DESC LIMIT 1 OFFSET 2)


DELETE FROM boxes WHERE value < 150;

DELETE FROM boxes WHERE warehouse IN
                        (SELECT w.code FROM warehouses w INNER JOIN boxes b ON w.code = b.warehouse
                                       WHERE w.location = 'New York' )
RETURNING *;


