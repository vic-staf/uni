--create database lab2;
/*create table countries(

    country_id serial primary key,
    country_name varchar(200),
    region_id integer,
    population integer

);

INSERT INTO countries( country_name, region_id, population)
VALUES ('Iceland', 1, 500000);

INSERT INTO countries( country_name)
VALUES ('Ireland');

INSERT INTO countries( country_name, region_id)
VALUES ('Finland', null);

INSERT INTO countries( country_name, region_id, population)
VALUES ('Greenland', 2, 100000),
       ('England', 3,1500000),
       ('Georgia', 4, 200000);

ALTER TABLE countries ALTER COLUMN country_name SET DEFAULT 'Kazakhstan';

INSERT INTO countries(region_id, population)
VALUES (5, 500000);

UPDATE countries SET country_name = DEFAULT;

CREATE TABLE countries_new
(LIKE countries);

INSERT INTO countries_new SELECT *FROM countries;

UPDATE countries SET region_id = 1 WHERE region_id IS NULL;

UPDATE countries SET population = population * 1.1;

SELECT country_name, population as "New population" FROM countries;

DELETE FROM countries
WHERE population < 100000;*/

DELETE FROM countries_new USING countries
WHERE ( countries.country_id) = ( countries_new.country_id);

DELETE FROM countries_new;





