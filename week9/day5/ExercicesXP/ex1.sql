SET search_path TO movies;

-- Task 1: Rank Movies by Popularity within Each Genre
-- Use the RANK() function to rank movies by their popularity within each genre. 
-- Display the genre name, movie title, and their rank based on popularity.
SELECT g.genre_name, m.title,
        RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity) AS rank
FROM movie m
JOIN movie_genres mg ON mg.movie_id = m.movie_id
JOIN genre g ON g.genre_id = mg.genre_id;



-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company
-- Use the NTILE() function to divide the movies produced by each production company into quartiles 
-- based on revenue. Display the company name, movie title, revenue, and quartile.
SELECT pc.company_name, m.title, m.revenue,
		NTILE(4) OVER (PARTITION BY pc.company_id ORDER BY m.revenue DESC) AS quartile
FROM movie m 
JOIN movie_company mc ON mc.movie_id = m.movie_id
JOIN production_company pc ON pc.company_id = mc.company_id
LIMIT(3);



-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre
-- Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets 
-- within each genre. Display the genre name, movie title, budget, and running total budget.
SELECT g.genre_name, m.title, m.budget,
		SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.budget DESC
							ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM movie m 
JOIN movie_genres mg ON mg.movie_id = m.movie_id
JOIN genre g ON g.genre_id = mg.genre_id;



-- Task 4: Identify the Most Recent Movie for Each Genre
-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. 
-- Display the genre name, movie title, and release date.
SELECT g.genre_name, m.title, m.release_date,
		FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_movie
FROM movie m 
JOIN movie_genres mg ON mg.movie_id = m.movie_id
JOIN genre g ON g.genre_id = mg.genre_id;



