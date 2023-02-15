--  script that lists all the cities of California that can be found in the database hbtn_0d_usa.
--  lists all the cities of California
USE hbtn_0d_usa;
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
AND states.name = 'California'
ORDER BY cities.id ASC;
