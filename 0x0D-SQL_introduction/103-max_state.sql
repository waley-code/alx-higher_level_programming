-- Displays the 3 cities with the highest average
-- temperatures between July and August.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`
