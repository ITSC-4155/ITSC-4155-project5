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

class Track(db.Model):
    __tablename__ = 'tracks'

    track_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, primary_key=False)
    duration = db.Column(db.Integer, primary_key=False)
    is_explicit = db.Column(db.Boolean, primary_key=False)
    audio_preview = db.Column(db.String, primary_key=False)
    release_date = db.Column(db.DateTime, primary_key=False)
    md5_image = db.Column(db.String, primary_key=False)
    track_position = db.Column(db.String, primary_key=False)
    artist_id = db.Column(db.Integer, primary_key=False)
    album_id = db.Column(db.Integer, primary_key=False)
    album_name = db.Column(db.String, primary_key=False)

    def __init__ \
    (self, track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id, album_name) -> None:
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
        self.album_name = album_name       

class Likes(db.Model):
    __tablename__ = 'likes'

    likes_id = db.Column (db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    def __init__ \
    (self, likes_id, id) -> None:
        self.likes_id = likes_id
        self.id = id

likes_tracklist = db.Table(
'likes_tracklist',
db.Column('likes_id', db.Integer,\
          db.ForeignKey('likes.likes_id', ondelete='CASCADE'), primary_key=True),
db.Column('track_id', db.Integer,\
          db.ForeignKey('tracks.track_id', ondelete='CASCADE'), primary_key=True),
)