from ..managers.user_manager import user_manager_class
from ..managers.track_manager import track_manager_class, duration
from ..managers.likes_manager import likes_manager_class

from ..models import db, User, Track
from flask_login import current_user


from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
import deezer

client = deezer.Client(app_id='foo', app_secret='bar')

api_pages = Blueprint('api', __name__, template_folder="templates", url_prefix='/api')


# These routers will be used for viewing and managing  Api - specific information


## Get an album page by ID
@api_pages.get('/album/<int:id>')
def showAlbum(id):

    album = client.get_album(id)
    likes = likes_manager_class.get_likes_by_id(current_user.id)
    mylikes = likes.tracks
  
       
    return render_template('album.html', album=album, likes = mylikes)




@api_pages.post('/track/<int:track_id>/like/')
def likeTrack(track_id):
    track = client.get_track(track_id)

    track_id = track_id
    title = track.title
    duration = track.duration
    is_explicit = track.explicit_lyrics
    audio_preview = track.preview
    release_date = track.release_date
    md5_image = track.md5_image
    track_position = track.track_position
    artist_id = track.artist.id
    album_id = track.album.id
    album_name = track.album.title

    track = Track.query.filter_by(track_id=track_id).first()
    
    if not track:
        track = track_manager_class.add_track(track_id, title, duration, is_explicit, audio_preview,\
        release_date, md5_image, track_position,artist_id, album_id, album_name) 
        db.session.add(track)
        db.session.commit()

    likes = likes_manager_class.get_likes_by_id(current_user.id)
    likes.tracks.append(track)

    db.session.commit()


    return redirect(f'/api/album/{album_id}')

@api_pages.post('/track/<int:track_id>/unlike/')
def unlikeTrack(track_id):

    track = client.get_track(track_id)

    gettrack = Track.query.filter_by(track_id=track_id).first()  
    likes = likes_manager_class.get_likes_by_id(current_user.id)
    likes.tracks.remove(gettrack)

    db.session.commit()
    return redirect(f'/api/album/{track.album.id}')



## Get an artist page by ID
@api_pages.get('/artist/<int:id>')
def showArtist(id):

    artist = client.get_artist(id)
    toptracks = client.get_artist(id).get_top()
    return render_template('artist.html', artist=artist, toptracks=toptracks)