-- lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
-- displays score and number of records in descending
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
