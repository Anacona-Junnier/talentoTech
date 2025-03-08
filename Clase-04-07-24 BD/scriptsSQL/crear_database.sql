CREATE DATABASE store;

USE store;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    categoria VARCHAR(255),
    cantidad INT
);

SELECT * FROM products;
