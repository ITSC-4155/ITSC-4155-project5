
CREATE TABLE IF NOT EXISTS users(
id SERIAL NOT NULL ,
email VARCHAR(255) NOT NULL,
username VARCHAR(30) NOT NULL,
"password" VARCHAR(255) NOT NULL,
profile_picture VARCHAR(255) NULL,
about VARCHAR(255) NULL,
PRIMARY KEY(id)
);




CREATE TABLE IF NOT EXISTS artists(
  artist_id BIGINT NOT NULL,
  "name" VARCHAR(200) NOT NULL,
  picture VARCHAR(300) NULL,
  fans INT NULL,
  PRIMARY KEY(artist_id)
);



CREATE TABLE IF NOT EXISTS albums(
  album_id BIGINT NOT NULL,
  title VARCHAR(255) NOT NULL,
  duration INT NOT NULL,
  num_tracks INT NOT NULL,
  is_explicit BOOLEAN NOT NULL,
  release_date DATE NOT NULL,
  record_type VARCHAR(255) NOT NULL,
  artist_id BIGINT NOT NULL,
PRIMARY KEY(album_id),
FOREIGN KEY(artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
);





CREATE TABLE IF NOT EXISTS tracks(
track_id BIGINT NOT NULL,
title VARCHAR(300) NOT NULL,
duration INT NOT NULL,
is_explicit BOOLEAN NOT NULL,
audio_preview VARCHAR(300) NOT NULL,
release_date DATE NOT NULL,
md5_image VARCHAR(300) NOT NULL,
track_position INT NOT NULL,
artist_id BIGINT NOT NULL,
album_id BIGINT NOT NULL,
PRIMARY KEY(track_id),
FOREIGN KEY(artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
FOREIGN KEY(album_id) REFERENCES albums(album_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS likes (
    likes_id SERIAL NOT NULL,
    id INT NOT NULL,
    PRIMARY KEY (likes_id),
    FOREIGN KEY (id) REFERENCES users(id) ON DELETE CASCADE 
);


CREATE TABLE IF NOT EXISTS likes_tracklist(
	track_id BIGINT,
	likes_id INT,
    PRIMARY KEY (track_id, likes_id),
    FOREIGN KEY (track_id) REFERENCES tracks(track_id) ON DELETE CASCADE,
    FOREIGN KEY (likes_id) REFERENCES likes(likes_id) ON DELETE CASCADE
);



CREATE TABLE IF NOT EXISTS track_contributors(
    artist_id BIGINT,
    track_id BIGINT,
    PRIMARY KEY (track_id, artist_id),
    FOREIGN KEY(track_id) REFERENCES tracks(track_id) ON DELETE CASCADE,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE
); 
    
CREATE TABLE IF NOT EXISTS playlists(
playlist_id SERIAL NOT NULL,
title VARCHAR(300) NOT NULL,
descr VARCHAR(255),
picture VARCHAR(300),
user_id INT NOT NULL,
PRIMARY KEY(playlist_id),
FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);




CREATE TABLE IF NOT EXISTS p_tracklist(
playlist_id INT NOT NULL,
track_id BIGINT NOT NULL,
PRIMARY KEY(track_id, playlist_id),
FOREIGN KEY(playlist_id) REFERENCES playlists(playlist_id) ON DELETE CASCADE,
FOREIGN KEY(track_id) REFERENCES tracks(track_id) ON DELETE CASCADE
);

