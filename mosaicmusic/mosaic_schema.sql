
CREATE TABLE IF NOT EXISTS users(
id SERIAL NOT NULL ,
email VARCHAR(255) NOT NULL,
username VARCHAR(30) NOT NULL,
"password" VARCHAR(255) NOT NULL,
profile_picture VARCHAR(255),
about VARCHAR(255),
PRIMARY KEY(id)
);

-- CREATE TABLE IF NOT EXISTS playlists(
-- playlist_id SERIAL NOT NULL,
-- title VARCHAR(300) NOT NULL,
-- descr VARCHAR(255),
-- picture VARCHAR(300),
-- link VARCHAR(300),
-- creator INT,
-- PRIMARY KEY(playlist_id),
-- FOREIGN KEY(creator) REFERENCES users(id) ON DELETE CASCADE,
-- );

-- CREATE TABLE IF NOT EXISTS p_tracklist(
-- playlist_id INT NOT NULL,
-- track_id INT NOT NULL,
-- PRIMARY KEY(track_id, playlist_id)
-- FOREIGN KEY(playlist_id) REFERENCES playlists(playlist_id) ON DELETE CASCADE,
-- FOREIGN KEY(track_id) REFERENCES tracks(track_id) ON DELETE CASCADE
-- );

-- CREATE TABLE IF NOT EXISTS albums(
--   album_id SERIAL NOT NULL,
--   title VARCHAR(255) NOT NULL,
--   duration INT NOT NULL,
--   num_tracks INT NOT NULL,
--   is_explicit INT NOT NULL,
--   release_date DATE NOT NULL,
--   record_type VARCHAR(255) NOT NULL,
--   artist_id INT NOT NULL,
-- PRIMARY KEY(album_id)
-- FOREIGN KEY(artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
-- );

-- CREATE TABLE IF NOT EXISTS tracks(
--   track_id SERIAL NOT NULL,
--   title VARCHAR(300) NOT NULL,
--   duration INT NOT NULL,
--   is_explicit BOOLEAN NOT NULL,
--   audio_preview VARCHAR(300) NOT NULL,
--   release_date DATE NOT NULL,
--   track_position INT NOT NULL,
--   artist_id INT NOT NULL,
--   album_id INT NOT NULL,
-- PRIMARY KEY(track_id),
-- FOREIGN KEY(album_id) REFERENCES albums(album_id) ON DELETE CASCADE,
-- FOREIGN KEY(artist_id) REFERENCES artsts(artist_id) ON DELETE CASCADE
-- );

-- CREATE TABLE IS NOT EXISTS a_tracklist(
-- album_id INT NOT NULL,
-- track_id INT NOT NULL,
-- PRIMARY KEY(track_id, album)
-- FOREIGN KEY(album_id) REFERENCES albums(album_id) ON DELETE CASCADE,
-- FOREIGN KEY(track_id) REFERENCES tracks(track_id) ON DELETE CASCADE
-- );

-- CREATE TABLE IS NOT EXISTS artists(
--   artist_id serial NOT NULL,
--   "name" VARCHAR(200) NOT NULL,
--   picture VARCHAR(300) NOT NULL,
--   fans INT NULL,
--   PRIMARY KEY(artist_id)
-- );

-- CREATE TABLE IF NOT EXISTS followers
--   (id INT NOT NULL, CONSTRAINT followers_pkey PRIMARY KEY(id));

-- CREATE TABLE IF NOT EXISTS genres(
--   genre_id SERIAL NOT NULL,
--   genre_name VARCHAR(30) NOT NULL,
--   album_id INT NULL,
--   PRIMARY KEY(genre_id)
--   FOREIGN KEY(album_id) REFERENCES albums(album_id) ON DELETE CASCADE
-- );

-- CREATE TABLE IF NOT EXISTS likes(
-- id INT NOT NULL,
-- track_id INT NOT NULL,
-- PRIMARY KEY (id, track_id),
-- FOREIGN KEY(id) REFERENCES users(id) ON DELETE CASCADE,
-- FOREIGN KEY(track_id) REFERENCES tracks(track_id) ON DELETE CASCADE 
-- );

-- CREATE TABLE public.profilefavs(
--     id serial NOT NULL, CONSTRAINT profilefavs_pkey PRIMARY KEY(id)
    
--     );

