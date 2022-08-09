--  a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- converting the database into utf8 format
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- converting the CHAR encoded table to utf8 format
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4;

-- converting a field in the table into utf8 format
ALTER TABLE hbtn_0c_0.first_table MODIFY `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

