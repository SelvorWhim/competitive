/* Some solutions are too short to get their own files... */

-- 595. Big Countries
SELECT name,population,area FROM World
	WHERE area > 3000000 OR population > 25000000;

-- 620. Not Boring Movies
SELECT id,movie,description,rating FROM cinema
    WHERE id%2=1 AND description != 'boring'
    ORDER BY rating DESC;

-- 627. Swap Salary
UPDATE salary SET sex=CASE
    WHEN sex='f' THEN 'm'
    WHEN sex='m' THEN 'f'
	END;
