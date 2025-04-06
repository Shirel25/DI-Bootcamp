-- 1. Count how many actors are in the table.
SELECT COUNT(*)
FROM actors;

-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
INSERT INTO actors (first_name, last_name, age)
VALUES ('Julia', 'Roberts', '1967-10-28');

-- OUTCOME: 
-- ERROR:  null value in column "number_oscars" violates not-null constraint
-- DETAIL:  Failing row contains (3, Julia, Roberts, 1967-10-28, null).
-- SQL state: 23502
-- --------------------------------------------------------------------------------------------------------
-- In this query, we tried to insert a new actor into the actors table without providing a value for the column number_oscars.
-- However, the table was defined with a NOT NULL constraint on this column, meaning it cannot accept empty or missing values.
-- As a result, PostgreSQL returns an error and does not insert the row.

