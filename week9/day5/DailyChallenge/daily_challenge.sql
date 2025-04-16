SET search_path TO movies;

-- 🌟 Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced. 
-- Use window functions to determine the budget growth rate and then calculate the average growth rate.

-- current and previous budget
WITH company_budgets AS (
	SELECT pc.company_id, pc.company_name, m.title, m.release_date, m.budget,
		LAG(m.budget) OVER (PARTITION BY pc.company_id ORDER BY m.release_date) AS prev_budget
	FROM movie m 
	JOIN movie_company mc ON mc.movie_id = m.movie_id
	JOIN production_company pc ON pc.company_id = mc.company_id
	WHERE m.budget IS NOT NULL
)

-- calculate the growth rate between the two successive films
, growth_calculation AS (
	SELECT company_name, title, release_date, budget, prev_budget,
		ROUND((budget - prev_budget)/ prev_budget, 4) AS growth_rate
	FROM company_budgets
	WHERE prev_budget > 0 AND budget IS NOT NULL
)

-- average growth rates per company
SELECT 
    company_name,
    ROUND(AVG(growth_rate) * 100, 2) AS avg_growth_rate_percent
FROM growth_calculation
GROUP BY company_name
ORDER BY avg_growth_rate_percent DESC
LIMIT 10;



-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. 
-- Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.

-- Average vote
WITH avg_rating_movies AS (
	SELECT AVG(m.vote_average) as avg_vote
	FROM movie m
)

-- Movies with vote > average vote
, high_rated_movies AS (
	SELECT m.movie_id, m.title, m.vote_average
	FROM movie m
	JOIN avg_rating_movies arm ON m.vote_average > arm.avg_vote
)

-- Actors who played in these movies
, actor_high_rated AS (
	SELECT p.person_name
	FROM high_rated_movies hrm
	JOIN movie_cast mc ON mc.movie_id = hrm.movie_id
	JOIN person p ON p.person_id = mc.person_id
)

SELECT person_name, COUNT(*) as nb_high_rated_movies
FROM actor_high_rated ahr
GROUP BY person_name
ORDER BY nb_high_rated_movies DESC
LIMIT 1;



-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies 
-- released in the genre. Use window functions with the ROWS frame specification to achieve this.
SELECT g.genre_name, m.title, m.release_date, m.revenue,
	ROUND(AVG(m.revenue) OVER (PARTITION BY g.genre_id ORDER BY m.release_date 
						ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) as rolling_avg_revenue
FROM movie m 
JOIN movie_genres mg ON mg.movie_id = m.movie_id
JOIN genre g ON g.genre_id = mg.genre_id;



-- 🌟 Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue. Use window functions 
-- and CTEs to group movies by their series and calculate the total revenue.
WITH movie_series AS (
	SELECT m.revenue, k.keyword_name
	FROM movie m 
	JOIN movie_keywords mk ON mk.movie_id = m.movie_id
	JOIN keyword k ON k.keyword_id = mk.keyword_id
)

, revenue_per_serie AS (
	SELECT keyword_name, SUM(revenue) as total_revenue,
		RANK() OVER (ORDER BY SUM(revenue) desc) as revenue_rank
	FROM movie_series
	GROUP BY keyword_name
)

SELECT *
FROM revenue_per_serie
WHERE revenue_rank = 1;