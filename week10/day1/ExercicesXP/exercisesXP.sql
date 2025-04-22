-- 🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis
-- Create a temporary table that join all tables and create a new one using LEFT JOIN. 
			-- Skipped temp table creation: direct LEFT JOIN for final dataset
-- Create an unique identifier code between the columns ‘employee_id’ and ‘date’ and call it ‘id’.
-- Convert the column ‘date’ to DATE type because it was previously configured as TIMESTAMP.
-- Transform this new table into a dataset “df_employee” for analysis.

CREATE TABLE df_employee AS
SELECT  
    s.employee_id || '_' || 
        substr(s.date, 7, 4) || '-' ||  -- year
        substr(s.date, 4, 2) || '-' ||  -- month
        substr(s.date, 1, 2) AS id,     -- day
    DATE(
        substr(s.date, 7, 4) || '-' || 
        substr(s.date, 4, 2) || '-' || 
        substr(s.date, 1, 2)
    ) AS month_year,          -- because date is in french format : "01/01/2022 00:00", must be "YYYY-MM-DD"
    s.employee_id, 
    s.employee_name,
    e."GEN(M_F)" AS gender,
    e.age,
    s.salary,
    f.function_group,
    c.company_name,
    c.company_city,
    c.company_state,
    c.company_type,
    c.const_site_category

FROM salaries s
LEFT JOIN employees e ON e.employee_code_emp = s.employee_id
LEFT JOIN functions f ON f.function_code = s.func_code
LEFT JOIN companies c ON c.company_name = s.comp_name;


------------------------------------------------------------------------------------------------------------------------------------------------
-- 🌟 Exercise 2: Cleaning Data for Consistency and Quality
--  run the following SQLite request and observe your new table.
SELECT * FROM df_employee;

--  Remove all unwanted spaces from all text columns using TRIM
UPDATE df_employee
SET
	id = TRIM(id),
    employee_id	= TRIM(employee_id),
	employee_name = TRIM(employee_name),
	gender = TRIM(gender),
    salary = TRIM(salary),
	function_group = TRIM(function_group),
	company_name = TRIM(company_name),
	company_city = TRIM(company_city),
	company_state = TRIM(company_state),
	company_type = TRIM(company_type),
	const_site_category = TRIM(const_site_category);

--  Check for NULL values and empty values.
SELECT *
FROM df_employee
WHERE id IS NULL
OR month_year IS NULL
OR employee_id IS NULL
OR employee_name IS NULL
OR gender IS NULL
OR age IS NULL
OR salary IS NULL
OR function_group IS NULL
OR company_name IS NULL
OR company_city IS NULL
OR company_state IS NULL
OR company_type IS NULL
OR const_site_category IS NULL
;

-- Delete rows of the detected missing values.
DELETE FROM df_employee
WHERE id = ''
	OR month_year = ''
	OR employee_id = ''
	OR employee_name = ''
	OR gender = ''
	OR age = ''
	OR salary = ''
	OR function_group = ''
	OR company_name = ''
	OR company_city = ''
	OR company_state = ''
	OR company_type = ''
	OR const_site_category = '';

-- company_city [correct typing]
UPDATE df_employee
SET company_city = 'Goiania'
WHERE company_city = 'Goianiaa';

------------------------------------------------------------------------------------------------------------------------------------------------
-- Checking standartization
UPDATE df_employee
SET gender = CASE gender
                 WHEN 'M' THEN 'Male'
                 WHEN 'F' THEN 'Female'
                 ELSE gender
             END;
   
   
UPDATE df_employee
SET const_site_category = 'Commercial'
WHERE const_site_category = 'Commerciall';

-- Check for duplicated rows in 'id' column.
SELECT DISTINCT id ,COUNT(id) as duplicated
FROM df_employee
GROUP BY id
HAVING COUNT(id) > 1;

	-- Check if the duplicates are indeed identical before deleting
SELECT *
FROM df_employee
WHERE id IN (
  SELECT id
  FROM df_employee
  GROUP BY id
  HAVING COUNT(*) > 1
)
ORDER BY id;


DELETE FROM df_employee
WHERE ROWID NOT IN (
  SELECT MIN(ROWID)
  FROM df_employee
  GROUP BY id
);


------------------------------------------------------------------------------------------------------------------------------------------------
-- 🌟 Exercise 3 : Calculating Current Employee Counts by Company
-- How many employees do the companies have today?
SELECT COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
WHERE month_year = (SELECT MAX(month_year)
                    FROM df_employee);

-- Group them by company
SELECT company_name, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
WHERE month_year = (SELECT MAX(month_year)
                    FROM df_employee)
GROUP BY company_name
ORDER BY employee_count DESC;


------------------------------------------------------------------------------------------------------------------------------------------------
-- 🌟 Exercise 4 : Analyzing Employee Distribution by City and Over Time
-- What is the total number of employees each city? Add a percentage column
SELECT  company_city, 
		COUNT(DISTINCT employee_id) as employee_count,
        (COUNT(DISTINCT employee_id) * 100) / SUM(COUNT(DISTINCT employee_id)) OVER() AS percentage
FROM df_employee
GROUP BY company_city
ORDER BY employee_count DESC;

-- What is the total number of employees each month?
SELECT month_year, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year
ORDER BY month_year DESC;

-- What is the average number of employees each month?
SELECT AVG(employee_count) AS monthly_counts
FROM (
  SELECT month_year, COUNT(DISTINCT employee_id) AS employee_count
  FROM df_employee
  GROUP BY month_year
);


------------------------------------------------------------------------------------------------------------------------------------------------
-- 🌟 Exercise 5 : Analyzing Employment Trends and Salary Metrics
-- What is the minimum and maximum number of employees throughout all the months? In which months were they?
  -- MAX
SELECT month_year, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year
ORDER BY employee_count DESC
LIMIT 1;

  -- MIN
SELECT month_year, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year
ORDER BY employee_count ASC
LIMIT 1; 

-- What is the monthly average number of employees by function group?
SELECT function_group, AVG(employee_count) AS avg_employees_per_month
FROM 
	(SELECT function_group, month_year, COUNT(DISTINCT employee_id) AS employee_count
     FROM df_employee
     GROUP BY function_group, month_year
	) AS monthly_counts
GROUP BY function_group
ORDER BY avg_employees_per_month DESC;

-- What is the annual average salary?
SELECT  substr(month_year, 1, 4) AS year, 
		AVG(CAST(salary AS REAL)) AS avg_salary_per_year
FROM df_employee
GROUP BY year;





