SET search_path TO movies;

-- Task 1: Rank Actors by Their Appearance in Movies
-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. 
-- Display the actor’s name and their rank.
SELECT person_name, 
		DENSE_RANK() OVER (ORDER BY total_movies DESC) AS actor_rank
FROM(
	SELECT p.person_name, COUNT(DISTINCT mc.movie_id) AS total_movies
	FROM movie_cast mc
	JOIN person p ON p.person_id = mc.person_id
	GROUP BY p.person_id
	) AS actors_counts;



-- Task 2: Identify the Top Director by Average Movie Rating
-- Use a CTE and the RANK() function to find the director with the highest average movie rating. 
-- Display the director’s name and their average rating.
WITH avg_director_rating AS (
	SELECT p.person_id, p.person_name, AVG(m.vote_average) AS avg_rating
	FROM movie_crew mc
	JOIN person p ON p.person_id = mc.person_id
	JOIN movie m ON m.movie_id = mc.movie_id
	WHERE mc.job = 'Director' 
	GROUP BY p.person_id, p.person_name
)
SELECT person_name, avg_rating,
	RANK() OVER (ORDER BY avg_rating DESC) AS rating_rank
FROM avg_director_rating
LIMIT 1;



-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor
-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. 
-- Display the actor’s name and the cumulative revenue.
SELECT p.person_name, m.revenue,
	SUM(m.revenue) OVER (PARTITION BY mc.person_id ORDER BY m.revenue
						ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_revenue
FROM movie m
JOIN movie_cast mc ON mc.movie_id = m.movie_id
JOIN person p ON p.person_id = mc.person_id; 



-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have the highest total budget. 
-- Display the director’s name and the total budget.
WITH director_budget AS (
    SELECT 
        mc.person_id,
        SUM(m.budget) AS total_budget
    FROM movie_crew mc
    JOIN movie m ON m.movie_id = mc.movie_id
    WHERE mc.job = 'Director'
    GROUP BY mc.person_id
)

SELECT 
    p.person_name,
    db.total_budget
FROM director_budget db
JOIN person p ON p.person_id = db.person_id
ORDER BY db.total_budget DESC
LIMIT 1;




