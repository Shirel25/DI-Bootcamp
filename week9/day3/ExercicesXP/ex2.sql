-- 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET language_id = 5 
WHERE film_id BETWEEN 1 and 5;

select * from film order by film_id;

-- 2. Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?

--> address_id is a foreign key to address(address_id)
-- When performing an INSERT INTO customer (...), we must:
-- 		Provide an address_id value that already exists in the address table.
-- 		Otherwise, the statement fails with a foreign key constraint violation error.

-- 3. We created a new table called customer_review. Drop this table. 
-- Is this an easy step, or does it need extra checking?
DROP TABLE customer_review; 

-- With foreign keys (film_id, language_id), the customer_review table depends on the others, 
-- but no other table depends on it. Doesn't need extra checking.

-- 4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT COUNT(*)
FROM rental
WHERE return_date IS NULL;

-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT f.title, f.rental_rate
FROM film f 
INNER JOIN inventory i 
	ON f.film_id = i.film_id
INNER JOIN rental r
	ON i.inventory_id = r.inventory_id
WHERE return_date IS NULL
ORDER BY f.rental_rate DESC
LIMIT 30; 

-- 6. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
-- but he can’t remember their names. Can you help him find which movies he wants to rent?

	-- 1. The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT f.title, f.description
FROM film f
JOIN film_actor fa 
	ON f.film_id = fa.film_id
JOIN actor a 
	ON fa.actor_id = a.actor_id
WHERE f.description ILIKE ('%sumo wrestler%')
	  and a.first_name = 'Penelope' 
	  and a.last_name = 'Monroe';

	-- 2. The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT title, length, rating
FROM film 
WHERE length < 60 and rating = 'R';

	-- 3. The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, 
	-- and he returned it between the 28th of July and the 1st of August, 2005.
SELECT f.title, c.first_name, c.last_name, p.amount, r.rental_date, r.return_date
FROM film f 
JOIN inventory i 
	ON f.film_id = i.film_id
JOIN rental r
	ON i.inventory_id = r.inventory_id
JOIN payment p
	ON r.rental_id = p.rental_id
JOIN customer c
	ON p.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' and last_name = 'Mahan'
	and p.amount > 4.00
	and r.return_date BETWEEN '2005-05-28' and '2005-08-01';

	--4. The 4th film : His friend Matthew Mahan watched this film, as well. It had the word 
	-- “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT f.title, f.description, f.replacement_cost
FROM film f 
JOIN inventory i 
	ON f.film_id = i.film_id
JOIN rental r
	ON i.inventory_id = r.inventory_id
JOIN payment p
	ON r.rental_id = p.rental_id
JOIN customer c
	ON p.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' and last_name = 'Mahan'
	and (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost desc;


-- SELECT * FROM film;
-- select * from payment; 
-- select * from rental;


