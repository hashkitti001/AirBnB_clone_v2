-- a script that prepares a MySQL server for testing purposes for the project
-- a script that prepares a MySQL server for the project
CREATE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema TO 'hbnb_test'@'localhost';
