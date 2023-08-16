-- Lists all record of the table second_table with score >=10
-- Results should display both the score and name
-- Score should be ordered
SELECT score, name
	FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;
