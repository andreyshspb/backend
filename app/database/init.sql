CREATE TABLE notes
(
    id        SERIAL PRIMARY KEY,
    author_id INT,
    topic     VARCHAR(255),
    content   VARCHAR(255)
);
