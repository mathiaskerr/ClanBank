DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS users;


CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    merchant_id INT NOT NULL REFERENCES merchants(id) ON DELETE CASCADE,
    tag VARCHAR(255),
    time VARCHAR(255),
    amount FLOAT
);
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    budget FLOAT
);