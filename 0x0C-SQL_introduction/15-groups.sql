-- List the number of records with the same score in the second table
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score DESC;
