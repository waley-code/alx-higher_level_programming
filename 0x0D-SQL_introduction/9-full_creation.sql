-- a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
-- creates a table second_table in the database hbtn_0c_0 
CREATE TABLE IF NOT EXISTS second_table (
	`id` INT AUTO_INCREMENT,
	`name` VARCHAR(256),
	`score` INT
);
INSERT INTO `second_table` (`name`, `score`) VALUES ("john", 10);
INSERT INTO `second_table` (`name`, `score`) VALUES ("Alex", 3);
INSERT INTO `second_table` (`name`, `score`) VALUES ("Bob", 14);
INSERT INTO `second_table` (`name`, `score`) VALUES ("George", 8);


