-- Lists the number of records with the sane score
SELECT score, COUNT(*) AS number
	FROM second_table
	GROUP BY score;
