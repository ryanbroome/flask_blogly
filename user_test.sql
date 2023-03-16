
DROP DATABASE IF EXISTS user_test_db;

CREATE DATABASE user_test_db;

\c user_test_db

DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  image_url VARCHAR(100)
);

INSERT INTO users (first_name, last_name, image_url)
VALUES ('RyanT', 'Broome', '/static/sample.jpeg');

INSERT INTO users (first_name, last_name, image_url)
VALUES ('BetsyT', 'Broome', '/static/sample.jpeg');

INSERT INTO users (first_name, last_name, image_url)
VALUES ('RomanT', 'Broome', '/static/sample.jpeg');

INSERT INTO users (first_name, last_name, image_url)
VALUES ('AveryT', 'Broome', '/static/sample.jpeg');