-- get list of tables
USE information_schema;
SELECT TABLE_NAME
FROM TABLES
WHERE TABLE_SCHEMA = 'mysql';
