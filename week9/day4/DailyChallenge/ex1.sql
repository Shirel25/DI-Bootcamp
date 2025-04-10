-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. Create a temporary 
-- table to store these competitors and their medal counts for each season, and then display the contents of this table.
CREATE TEMP TABLE competitors_medals_by_season AS
SELECT ce.competitor_id, g.season, COUNT(*) AS nb_medals
FROM competitor_event ce
JOIN games_competitor gc ON gc.person_id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
GROUP BY ce.competitor_id, g.season;

CREATE TEMP TABLE competitors_winning AS
SELECT competitor_id
FROM competitors_medals_by_season
GROUP BY competitor_id
HAVING COUNT(DISTINCT season) = 2;

SELECT cw.competitor_id, cms.season, cms.nb_medals
FROM competitors_winning cw
JOIN competitors_medals_by_season cms
ON cw.competitor_id = cms.competitor_id;



-- Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to 
-- identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.
CREATE TEMP TABLE competitors_medals_by_sport AS
SELECT ce.competitor_id, s.sport_name, COUNT(*) AS nb_medals
FROM competitor_event ce 
JOIN event e ON ce.event_id = e.id
JOIN sport s ON s.id = e.sport_id
GROUP BY ce.competitor_id, s.sport_name;

CREATE TEMP TABLE medals_two_sports AS 
SELECT competitor_id
FROM competitors_medals_by_sport
GROUP BY competitor_id
HAVING COUNT(DISTINCT sport_name) = 2;


SELECT cms.competitor_id, SUM(cms.nb_medals) AS total_medals
FROM competitors_medals_by_sport cms
JOIN medals_two_sports m2s ON cms.competitor_id = m2s.competitor_id
GROUP BY cms.competitor_id
ORDER BY total_medals DESC
LIMIT 3;
