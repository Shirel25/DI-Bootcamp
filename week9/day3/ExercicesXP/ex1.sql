-- 1. Get a list of all the languages, from the language table.
SELECT * FROM language; 

-- 2. Get a list of all films joined with their languages –
-- select the following details : film title, description, and language name.
SELECT f.title, f.description, l.name
FROM film f
INNER JOIN language l
ON f.language_id = l.language_id;

-- 3. Get all languages, even if there are no films in those languages – 
-- select the following details : film title, description, and language name.
SELECT f.title, f.description, l.name
FROM film f
FULL JOIN language l
ON f.language_id = l.language_id;

-- 4. Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film(
id SERIAL PRIMARY KEY,
name TEXT
);

INSERT INTO new_film(name)
VALUES 
		('Wonder Woman'),
		('Harry Potter'),
		('Interstellar');

-- 5. Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
CREATE TABLE customer_review(
review_id SERIAL PRIMARY KEY,
film_id INTEGER REFERENCES new_film (id) ON DELETE CASCADE,
language_id INTEGER REFERENCES language (language_id) ON DELETE CASCADE,
title TEXT,
score INTEGER CHECK (score BETWEEN 1 and 10),
review_text TEXT,
last_update DATE
);

-- 6. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update)
VALUES 
		(1, 1, 'Wonder Woman', 10, 'One of my favorite movies! So gripping!', CURRENT_DATE),
		(2, 5, 'Harry Potter', 10, 'L''un des films d''une série incroyable! Je recommande vivement!', CURRENT_DATE);
		-- (3, 1, 'Interstellar', 3, 'Sorry... I hate the space...', CURRENT_DATE);

SELECT * FROM customer_review;

-- 7. Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film f 
USING customer_review cr
WHERE f.id = cr.film_id;

SELECT * FROM new_film;
-- It deletes movies from new_film that have an associated review.
-- And since we set ON DELETE CASCADE in customer_review,
-- the related reviews will also be automatically deleted.