-- 1. OUTPUT: 0
SELECT COUNT(*) 
    FROM FirstTab AS ft 
	WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL ) -- NOT IN (NULL)

-- ft.id	Does ft.id NOT IN (NULL)?	Result SQL
-- 5			5 NOT IN (NULL)			 UNKNOWN Because we can't compare a value to NULL directly.
-- 6			6 NOT IN (NULL)			 UNKNOWN SQL can't tell if 5 ≠ NULL, so it says "I don't know" → UNKNOWN
-- 7			7 NOT IN (NULL)			 UNKNOWN
-- NULL			NULL NOT IN (NULL)		 UNKNOWN

-- SQL only keeps rows where the condition is TRUE.
-- Here, they are all UNKNOWN → so no rows are selected.

-- 2. OUTPUT: 2
SELECT COUNT(*) 
    FROM FirstTab AS ft 
	WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 ) -- NOT IN (5)

-- ft.id	Does ft.id NOT IN (5)?	Result SQL
-- 5			5 NOT IN (5)		 FALSE 
-- 6			6 NOT IN (5)		 TRUE 
-- 7			7 NOT IN (5)		 TRUE
-- NULL			NULL NOT IN (5)		 UNKNOWN

-- 3. OUTPUT: 0
SELECT COUNT(*) 
    FROM FirstTab AS ft 
	WHERE ft.id NOT IN ( SELECT id FROM SecondTab ) -- NOT IN (5, NULL)

-- ft.id	Does ft.id NOT IN (5, NULL)?	   Result SQL
-- 5			5 NOT IN (5, NULL)		 		UNKNOWN 
-- 6			6 NOT IN (5, NULL)		 		UNKNOWN 
-- 7			7 NOT IN (5, NULL)		 		UNKNOWN
-- NULL			NULL NOT IN (5, NULL)		 	UNKNOWN

-- If the list in a NOT IN contains NULL, then the whole test becomes UNKNOWN for each line
-- When there is a single NULL in the NOT IN, it negates the entire condition.

--4. OUTPUT: 2
SELECT COUNT(*) 
   FROM FirstTab AS ft 
   WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL ) -- NOT IN (5)

-- ft.id	Does ft.id NOT IN (5)?	   Result SQL
-- 5			5 NOT IN (5)		 	 FALSE
-- 6			6 NOT IN (5)		 	 TRUE
-- 7			7 NOT IN (5)		 	 TRUE
-- NULL			NULL NOT IN (5)		    UNKNOWN	