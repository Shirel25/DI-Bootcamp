-- Task 1: Update the heights of competitors based on the average height of competitors from the same region. 
-- Use a correlated subquery within the UPDATE statement.
UPDATE person
SET height = (
  SELECT AVG(p2.height) FROM person p2
  JOIN person_region pr2 ON p2.id = pr2.person_id
  WHERE pr2.region_id = (
    SELECT pr.region_id FROM person_region pr
    WHERE pr.person_id = person.id)
  AND p2.height != 0
)
WHERE height = 0;

select height from person where height = 0;



-- Task 2: Insert new records into a temporary table for competitors who participated in more 
-- than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.
CREATE TEMP TABLE multi_event_competitors AS
SELECT gc.games_id, gc.person_id, COUNT(DISTINCT ce.event_id) AS nb_events
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
GROUP BY gc.games_id, gc.person_id
HAVING nb_events > 1;


select * from multi_event_competitors;



-- Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. 
-- Use subqueries to calculate and compare averages.
SELECT region_name, AVG(medal_count) AS avg_medals_per_competitor
FROM (
  SELECT r.region_name, ce.competitor_id, COUNT(ce.medal_id) AS medal_count
  FROM competitor_event ce
  JOIN games_competitor gc ON gc.id = ce.competitor_id
  JOIN person_region pr ON pr.person_id = gc.person_id
  JOIN noc_region r ON pr.region_id = r.id
  WHERE ce.medal_id IS NOT NULL
  GROUP BY r.region_name, ce.competitor_id
) AS region_medals
GROUP BY region_name
HAVING AVG(medal_count) > (
  SELECT AVG(total_medals)
  FROM (
    SELECT competitor_id, COUNT(medal_id) AS total_medals
    FROM competitor_event
    WHERE medal_id IS NOT NULL
    GROUP BY competitor_id
  )
);



-- Task 4: Create a temporary table to track competitors’ participation across different seasons and 
-- identify those who have participated in both Summer and Winter games.
create temp table competitors_participation AS
select gc.person_id, g.season
from games g
join games_competitor gc On gc.games_id = g.id;

select * from competitors_participation;









