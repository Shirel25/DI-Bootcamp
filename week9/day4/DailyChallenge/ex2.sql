-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. 
-- Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 
-- regions with the highest total medals.

-- Number of medals per competitor and per event
CREATE TEMP TABLE competitor_event_medals AS
SELECT ce.competitor_id, ce.event_id, COUNT(ce.medal_id) AS nb_medals
FROM competitor_event ce
GROUP BY ce.competitor_id, ce.event_id;

SELECT * FROM competitor_event_medals;

-- Their best event
CREATE TEMP TABLE best_event_per_competitor AS
SELECT competitor_id, MAX(nb_medals) AS max_medals
FROM competitor_event_medals
GROUP BY competitor_id;

SELECT * FROM best_event_per_competitor;

-- Join the two temporary table to find the associated event.
CREATE TEMP TABLE top_event_details AS
SELECT cem.competitor_id, cem.event_id, cem.nb_medals
FROM competitor_event_medals cem
JOIN best_event_per_competitor bepc
ON cem.competitor_id = bepc.competitor_id
AND cem.nb_medals = bepc.max_medals;

SELECT * FROM top_event_details;

-- Add regions
CREATE TEMP TABLE top_event_regions AS
SELECT r.region_name, t.nb_medals
FROM top_event_details t
JOIN games_competitor gc ON gc.id = t.competitor_id
JOIN person_region pr ON pr.person_id = gc.person_id
JOIN noc_region r ON r.id = pr.region_id;

SELECT DISTINCT * FROM top_event_regions;

-- Show Top 5 Regions
SELECT region_name, SUM(nb_medals) AS total_medals
FROM top_event_regions
GROUP BY region_name
ORDER BY total_medals DESC
LIMIT 5;



-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any 
-- medals. Retrieve and display the contents of this table, including their full names and the number of games they participated in.
CREATE TEMP TABLE competitor_participation AS 
SELECT gc.person_id, COUNT(DISTINCT gc.games_id) AS total_games
FROM games_competitor gc
LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id
WHERE ce.medal_id IS NULL
GROUP BY gc.person_id
HAVING COUNT(DISTINCT gc.games_id) > 3;


SELECT cp.person_id, p.full_name, cp.total_games
FROM competitor_participation cp
JOIN person p ON p.id = cp.person_id;






