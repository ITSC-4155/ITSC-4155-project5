from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile_picture = db.Column(db.String, nullable=True)
    about = db.Column(db.String, nullable=True) 
    
    
    def __init__(self, email, username, password) -> None:
        self.email = email
        self.username = username
        self.password = password
        self.profile_picture = ''
        self.about = ''


class Artist(db.Model):
    __tablename__ = 'artists'

    artist_id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String, primary_key=False)
    picture = db.Column(db.String, primary_key=False)
    fans = db.Column(db.Integer, primary_key=False)
    tracks = db.relationship('Track', backref='artist', passive_deletes=True)
        
    def __init__(self, artist_id, name ) -> None:
        self.artist_id = artist_id
        self.name = name



class Album(db.Model):
    __tablename__ = 'albums'
        
    album_id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String, primary_key=False)
    duration = db.Column(db.Integer, primary_key=False)
    num_tracks =  db.Column(db.Integer, primary_key=False)
    is_explicit = db.Column(db.Boolean, primary_key=False)
    release_date = db.Column(db.DateTime, primary_key=False)
    record_type = db.Column(db.String, primary_key=False)
    artist_id = db.Column(db.BigInteger, db.ForeignKey('artists.artist_id',  ondelete='CASCADE'), nullable=False)
    tracks = db.relationship('Track', backref='album', passive_deletes=True)

    def __init__(self, album_id, title, duration, num_tracks, is_explicit, release_date, \
                     record_type, artist_id ) -> None:
        self.album_id = album_id
        self.title = title
        self.duration = duration
        self.num_tracks = num_tracks
        self.is_explicit = is_explicit
        self. release_date = release_date
        self.record_type = record_type
        self.artist_id = artist_id


track_contributors = db.Table(
'track_contributors',
db.Column('track_id', db.BigInteger,\
          db.ForeignKey('tracks.track_id', ondelete='CASCADE'), primary_key=True),
db.Column('artist_id', db.BigInteger,\
          db.ForeignKey('artists.artist_id', ondelete='CASCADE'), primary_key=True),
)


class Track(db.Model):
    __tablename__ = 'tracks'

    track_id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String, primary_key=False)
    duration = db.Column(db.Integer, primary_key=False)
    is_explicit = db.Column(db.Boolean, primary_key=False)
    audio_preview = db.Column(db.String, primary_key=False)
    release_date = db.Column(db.DateTime, primary_key=False)
    md5_image = db.Column(db.String, primary_key=False)
    track_position = db.Column(db.String, primary_key=False)
    artist_id = db.Column(db.BigInteger, db.ForeignKey('artists.artist_id',  ondelete='CASCADE'), nullable=False)
    album_id = db.Column(db.BigInteger, db.ForeignKey('albums.album_id',  ondelete='CASCADE'), nullable=False)
    contributors = db.relationship('Artist', secondary=track_contributors, backref='artists', passive_deletes=True)

    def __init__ \
    (self, track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id) -> None:
        self.track_id = track_id
        self.title = title
        self.duration = duration
        self.is_explicit = is_explicit
        self.audio_preview = audio_preview
        self.release_date = release_date
        self.md5_image = md5_image
        self.track_position = track_position
        self.artist_id = artist_id
        self.album_id = album_id
      


likes_tracklist = db.Table(
'likes_tracklist',
db.Column('likes_id', db.Integer,\
          db.ForeignKey('likes.likes_id', ondelete='CASCADE'), primary_key=True),
db.Column('track_id', db.BigInteger,\
          db.ForeignKey('tracks.track_id', ondelete='CASCADE'), primary_key=True),
)


class Likes(db.Model):
    __tablename__ = 'likes'

    likes_id = db.Column (db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    tracks = db.relationship('Track', secondary=likes_tracklist, backref='likes', passive_deletes=True)

    def __init__ \
    (self, likes_id, id) -> None:
        self.likes_id = likes_id
        self.id = id

