-- Import in hbtn_0c_0 database this table dump
-- Import in hbtn_0c_0 database this table dump
SELECT AVG(`value`) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
