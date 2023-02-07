CREATE USER web;
CREATE DATABASE web;
GRANT ALL PRIVILEGES ON DATABASE web TO web;

CREATE TABLE IF NOT EXISTS web.user (
    user_id serial PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO web.user (
    user_id,
    username,
    password_hash,
    email
) VALUES (
    1,
    "first_user",
    "some_hash",
    "first@user.ru"
)

INSERT INTO web.user (
    user_id,
    username,
    password_hash,
    email
) VALUES (
    2,
    "second_user",
    "some_hash",
    "second@user.ru"
)