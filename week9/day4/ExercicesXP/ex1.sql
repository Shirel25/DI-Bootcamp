-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won.
-- Use a correlated subquery to achieve this.
select m.medal_name, 
    (select AVG(gc.age) from games_competitor gc
    INNER JOIN competitor_event ce ON gc.id = ce.competitor_id
    WHERE ce.medal_id = m.id AND gc.age IS NOT NULL) as avg_age
from medal m;
-- GROUP BY is not needed in the main query because we are
-- selecting one row per medal from the medal table.



-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 
-- different events. Use nested subqueries to filter and aggregate the data.
SELECT nr.region_name, COUNT(DISTINCT pr.person_id) AS competitor_count
FROM noc_region nr
JOIN person_region pr ON pr.region_id = nr.id
WHERE pr.person_id IN (
    SELECT gc.person_id
    FROM games_competitor gc
    JOIN competitor_event ce ON gc.id = ce.competitor_id
    GROUP BY gc.person_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
)
GROUP BY nr.region_name
ORDER BY competitor_count DESC
LIMIT 5;



-- Task 3: Create a temporary table to store the total number of medals won by each competitor and 
-- filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.

-- Create the temporary table
CREATE TEMP TABLE total_medals (
  competitor_id INTEGER,
  medals_id INTEGER
 );
 
 -- Populate the table 
 INSERT INTO total_medals(competitor_id, medals_id)
 select competitor_id, medal_id
 FROM competitor_event
 WHERE medal_id IS NOT NULL;
 
 -- Query: competitors with more than 2 medals
 select competitor_id, COUNT(*) AS total_medals 
 from total_medals
 GROUP BY competitor_id
 HAVING COUNT(*) > 2;
 
 -- Drop the temporary table to free resources
DROP TABLE total_medals;



-- Task 4: Use a subquery within a DELETE statement to remove records of competitors who have 
-- not won any medals from a temporary table created for analysis.

-- Create the temporary table and populate table
CREATE TEMP TABLE all_competitors AS
SELECT gc.id AS competitor_id, gc.person_id, ce.medal_id
FROM games_competitor gc
LEFT JOIN competitor_event ce ON gc.person_id = ce.competitor_id;

-- Delete 
DELETE FROM all_competitors
WHERE medal_id IS NULL;

-- Supposed to return nothing
SELECT * FROM all_competitors
WHERE medal_id IS NULL;

-- Other verification
SELECT medal_id, COUNT(*) 
FROM all_competitors
GROUP BY medal_id;

--  Drop the temporary table to free resources
DROP TABLE all_competitors;



