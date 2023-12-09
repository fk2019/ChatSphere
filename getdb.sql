-- create db and user
CREATE DATABASE IF NOT EXISTS chatdb;
USE chatdb;

CREATE USER IF NOT EXISTS chat_user@localhost IDENTIFIED BY 'chat';

GRANT ALL PRIVILEGES ON chatdb.* TO chat_user@localhost;
SHOW TABLES;
