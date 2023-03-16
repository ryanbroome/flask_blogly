
DROP DATABASE IF EXISTS users_db;

CREATE DATABASE users_db;

\c users_db

DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  image_url VARCHAR(100)
);

INSERT INTO users (first_name, last_name, image_url)
VALUES ('Ryan', 'Broome', '/static/sample.jpeg');

INSERT INTO users (first_name, last_name, image_url)
VALUES ('Betsy', 'Broome', '/static/sample.jpeg');

INSERT INTO users (first_name, last_name, image_url)
VALUES ('Roman', 'Broome', '/static/sample.jpeg');

INSERT INTO users (first_name, last_name, image_url)
VALUES ('Avery', 'Broome', '/static/sample.jpeg');