-- Create a table on a MYSQL server with ID being unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT '1' UNIQUE, name VARCHAR(256));
