-- creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows
-- creates a full table
CREATE second_table IF NOT EXISTS (id INT, name VARCHAR(256), score INT);
-- set new row
INSERT INTO `second_table` (`id`, `name`, `score`) (1, 'John', 10);
INSERT INTO `second_table` (`id`, `name`, `score`) (2, 'Alex', 3);
INSERT INTO `second_table` (`id`, `name`, `score`) (3, 'Bob', 14);
INSERT INTO `second_table` (`id`, `name`, `score`) (4, 'George', 8);
