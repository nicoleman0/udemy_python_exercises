-- to run this file in SQLite3, use: .read example.sql

CREATE TABLE cats

(
    name TEXT,
    breed TEXT,
    age INTEGER
);

INSERT INTO cats (name, breed, age)
VALUES
    ('Mittens', 'Siamese', 2),
    ('Whiskers', 'Tabby', 5),
    ('Fluffy', 'Persian', 3),
    ('Franky', 'Russian Blue', 4);

CREATE TABLE dogs
(
    name TEXT,
    breed TEXT,
    age INTEGER
);
INSERT INTO dogs (name, breed, age)
VALUES
    ('Buddy', 'Golden Retriever', 3),
    ('Max', 'Bulldog', 4),
    ('Bella', 'Beagle', 2),
    ('Charlie', 'Poodle', 5);