-- ========================================== Part I ==========================================

-- 1. Create 2 tables : Customer and Customer profile. They have a One to One relationship.
CREATE TABLE customer(
customer_id SERIAL,
first_name VARCHAR(45),
last_name VARCHAR(45) NOT NULL,
PRIMARY KEY (customer_id)
);

CREATE TABLE customer_profile(
customer_profile_id INTEGER,
is_logged_in BOOLEAN DEFAULT FALSE, 
PRIMARY KEY (customer_profile_id),
CONSTRAINT fk_customer_id FOREIGN KEY (customer_profile_id) REFERENCES customer(customer_id)
);

-- 2. Insert customers
INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe'),
		('Jerome', 'Lalu'),
		('Lea', 'Rive');

SELECT * FROM customer;

-- 3. Insert customer profiles, use subqueries
INSERT INTO customer_profile(customer_profile_id, is_logged_in)
VALUES ((SELECT customer_id FROM customer WHERE first_name = 'John'), TRUE),
	   ((SELECT customer_id FROM customer WHERE first_name = 'Jerome'), FALSE);

SELECT * FROM customer_profile;

-- 4. Use the relevant types of Joins to display:
	-- 1. The first_name of the LoggedIn customers
SELECT c.first_name FROM customer c
INNER JOIN customer_profile cp ON c.customer_id = cp.customer_profile_id
WHERE cp.is_logged_in = TRUE;

	-- 2. All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT c.first_name, cp.is_logged_in
FROM customer c
LEFT JOIN customer_profile cp ON c.customer_id = cp.customer_profile_id;

	-- 3. The number of customers that are not LoggedIn
SELECT COUNT(*)
FROM customer c 
INNER JOIN customer_profile cp ON c.customer_id = cp.customer_profile_id
WHERE cp.is_logged_in = FALSE;


-- ========================================== Part II ==========================================

-- 1. Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
CREATE TABLE book (
book_id SERIAL PRIMARY KEY,
title TEXT NOT NULL,
author VARCHAR(45) NOT NULL
);

-- 2. Insert books 
INSERT INTO book (title, author)
VALUES ('Alice In Wonderland', 'Lewis Carroll'),
	   ('Harry Potter', 'J.K Rowling'),
	   ('To kill a mockingbird', 'Harper Lee');

SELECT * FROM book;

-- 3. Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE,
-- age. Make sure that the age is never bigger than 15 (Find an SQL method);
CREATE TABLE student (
student_id SERIAL PRIMARY KEY, 
name VARCHAR(45) NOT NULL UNIQUE,
age INTEGER CHECK (age <= 15)
);

-- 4. Insert students
INSERT INTO student (name, age)
VALUES ('John', 12),
	   ('Lera', 11),
	   ('Patrick', 10),
	   ('Bob', 14);

SELECT * FROM student;

-- 5. Create a table named Library
CREATE TABLE library (
book_fk_id INTEGER NOT NULL,
student_fk_id INTEGER NOT NULL,
borrowed_date DATE,
PRIMARY KEY (book_fk_id, student_fk_id),
FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- 6. Add 4 records in the junction table, use subqueries
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES	((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
		 (SELECT student_id FROM student WHERE name = 'John'),
		 '15/02/2022'),
		((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
		 (SELECT student_id FROM student WHERE name = 'Bob'),
		 '03/03/2021'),
		((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
		 (SELECT student_id FROM student WHERE name = 'Lera'),
		 '23/05/2021'),
		((SELECT book_id FROM book WHERE title = 'Harry Potter'),
		 (SELECT student_id FROM student WHERE name = 'Bob'),
		 '12/08/2021');

-- 7. Display the data
	-- 1. Select all the columns from the junction table
SELECT * FROM library;

	-- 2. Select the name of the student and the title of the borrowed books
SELECT s.name, b.title
FROM library l 
INNER JOIN student s ON l.student_fk_id = s.student_id
INNER JOIN book b ON l.book_fk_id = b.book_id;

	-- 3. Select the average age of the children, that borrowed the book Alice in Wonderland
SELECT AVG(s.age)
FROM student s
INNER JOIN library l ON l.student_fk_id = s.student_id
INNER JOIN book b ON l.book_fk_id = b.book_id
WHERE b.title ILIKE 'Alice in Wonderland';

	-- 4. Delete a student from the Student table, what happened in the junction table ?
DELETE FROM student
WHERE name = 'John';

SELECT * FROM student;
SELECT * FROM library;

-- When I deleted the student named John, his corresponding borrow records in the library 
-- table were also deleted automatically because of the ON DELETE CASCADE constraint on the foreign key.

