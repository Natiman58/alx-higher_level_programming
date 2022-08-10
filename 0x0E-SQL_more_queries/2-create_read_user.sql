--  a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn_0d_2 already exists, your script should not fail
-- If the user user_0d_2 already exists, your script should not fail

-- creating the data base
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creating the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- granting only SELECT privilege to the user
GRANT SELECT on hbtn_0d_2.* TO 'user_0d_2'@'localhost'; 

