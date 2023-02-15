-- script that creates the database hbtn_0d_2 and the user user_0d_2.
-- creates the database hbtn_0d_2 and the user user_0d_2 with the specified privileges and password, while also ensuring that the script does not fail if the database or user already exists:
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
