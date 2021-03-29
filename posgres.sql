
WORK ON northwind

---install---
sudo apt install postgresql
sudo systemctl is-active postgresql
sudo systemctl is-enabled postgresql
sudo systemctl status postgresql
sudo systemctl is-active postgresql
sudo systemctl is-enabled postgresql
sudo systemctl status postgresql



sudo apt install pgadmin4

sudo systemctl restart postgresql

sudo su - postgres
psql

 ---select all---

SELECT *
FROM employees;



---select fields---

SELECT first_name,
       last_name
FROM employees;



---distnict---

SELECT DISTINCT country,
                city
FROM customers;



---count---

SELECT count(*)
FROM customers;



---distnict , count---

SELECT count(DISTINCT country)
FROM customers;



---where---

SELECT *
FROM customers
WHERE country='Germany';



---and---

SELECT *
FROM customers
WHERE country='Germany'
  AND city='Berlin';



---or---

SELECT *
FROM customers
WHERE country='Germany'
  OR city='Berlin';



---not---

SELECT *
FROM customers
WHERE NOT city='Paris';



---between---

SELECT *
FROM order_details
WHERE unit_price BETWEEN 10 AND 43;



---list search---

SELECT *
FROM customers
WHERE country in ('France',
                  'USA',
                  'Germany');



---ordering---

SELECT DISTINCT country,
                city
FROM customers
ORDER BY country ASC,
         city DESC;



---aggregate---

SELECT max(unit_price),
       min(unit_price),
       avg(unit_price),
       sum(unit_price)
FROM order_details;



---mathmathic---

SELECT unit_price * quantity
FROM order_details;


SELECT unit_price + quantity
FROM order_details;


SELECT unit_price / quantity
FROM order_details;


SELECT customer_id,
       shipped_date - order_date
FROM orders;



---patterns---

SELECT *
FROM customers
WHERE company_name like 'A%';


SELECT *
FROM customers
WHERE company_name like 'A%e';



--- % all charaacter ---

SELECT *
FROM customers
WHERE company_name like 'A%i%';



--- _ one character ---

SELECT *
FROM customers
WHERE company_name like 'A_f%';



--- as(name for field) ---

SELECT unit_price * quantity AS multy
FROM order_details;



---limit---

SELECT unit_price * quantity AS total
FROM order_details
ORDER BY total DESC
LIMIT 7;



---is---

SELECT company_name,
       region
FROM customers
WHERE region IS NOT NULL;


SELECT company_name,
       region
FROM customers
WHERE region IS NULL;



--- inner join---

SELECT country,
       phone,
       order_date,
       ship_country
FROM customers
JOIN orders ON orders.customer_id=customers.customer_id 



--- right join ---

SELECT company_name,
       order_id
FROM customers
RIGHT JOIN orders ON orders.customer_id=customers.customer_id 



---left join ---

SELECT company_name,
       order_id
FROM customers
LEFT JOIN orders ON orders.customer_id=customers.customer_id 



---full join ---

SELECT company_name,
       order_id
FROM customers
FULL JOIN orders ON orders.customer_id=customers.customer_id 



---self join---

SELECT e1.birth_date,
       e2.birth_date
FROM employees e1,
               employees e2
WHERE e1.birth_date > e2.birth_date 



---group by---

  SELECT country,
         count(*)
  FROM customers
GROUP BY country;


SELECT company_name,
       count(freight),
       round(sum(freight))
FROM customers
JOIN orders ON orders.customer_id=customers.customer_id
GROUP BY company_name
ORDER BY round DESC;



---having---

SELECT product_name,
       sum(quantity*order_details.unit_price) AS total
FROM order_details
JOIN products ON products.product_id=order_details.product_id
JOIN orders ON orders.order_id=order_details.order_id
WHERE order_date BETWEEN '1997-01-01' AND '1997-12-31'
GROUP BY product_name
HAVING sum(quantity*order_details.unit_price) > 2000
ORDER BY total ASC;



---union---

SELECT company_name
FROM customers
UNION
SELECT company_name
FROM suppliers;


SELECT city
FROM customers
UNION ALL
SELECT city
FROM suppliers;



---insert into---

INSERT INTO customers (customer_id, company_name, country)
VALUES ('joe', 'loutus', 'USA');



---update---

UPDATE customers
SET company_name='apple',
    country='USK'
WHERE customer_id='joe';



---delete---

DELETE
FROM customers
WHERE customer_id='joe';



---select into---

SELECT * INTO testing
FROM customers
WHERE country in('USA',
                 'USK');



---insert into select---

INSERT INTO testing
SELECT *
FROM customers
WHERE coutry='Germany';


INSERT INTO testing (cilumn1,....)
SELECT column1,...
FROM customers
WHERE coutry='Germany';



--- create,drop DB---

CREATE DATABASE joe;


DROP DATABASE joe;



---table---

CREATE TABLE me (
		id Int PRIMARY KEY,
                user_name varchar(60) UNIQUE,
                age Int NOT NULL CONSTRAINT ch_age CHECK (age>10),
                register date,
                is_admin boolean DEFAULT FALSE,
                fk varchar(10) UNIQUE,
                FOREIGN KEY (fk) REFERENCES customers(customer_id),
                CONSTRAINT usernaem CHECK LENGTH(username)
                );


ALTER TABLE me RENAME username TO firstname
ALTER TABLE me RENAME TO users;


ALTER TABLE users ADD birth_date varchar(300);


ALTER TABLE users
DROP birth_date;


ALTER TABLE users
ALTER COLUMN user_name TYPE varchar(330);


CREATE UNIQUE INDEX username_users ON users(user_name);


DROP INDEX username_users;
￼

----postgres in django----
>>> sudo su - postgres
>>> psql
CREATE DATABASE myproject;

CREATE USER myprojectuser WITH PASSWORD 'password';

ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;


---select DB---
\c DB_name
\connect DB_name

---show DB---
\l

---show,delete user---
\du
\du+

DROP USER user_name;


------BACKUP--------
pg_dump dbname > dumpfile
psql dbname < dumpfile  ----Restoring the Dump

-----POSTGRES IN PYTHON-----



