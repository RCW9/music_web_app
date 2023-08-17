
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;


CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER,
    artist_id INTEGER
);


INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
