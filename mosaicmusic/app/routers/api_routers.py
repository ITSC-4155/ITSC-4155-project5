from ..managers.user_manager import user_manager_class
from ..managers.api_manager import api_manager_class
from ..managers.likes_manager import likes_manager_class

from ..models import db, User, Track, Artist
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

    # search for artist in local DB, add artist if not there
    getartist = api_manager_class.get_artist_by_id(track.artist.id)
    if not getartist:
        artist_id = track.artist.id
        name = track.artist.name
        artist = api_manager_class.add_artist(artist_id, name)
        db.session.add(artist)
      
    
    # search for album in local DB, add album if not there
    getalbum = api_manager_class.get_album_by_id(track.album.id)
    if not getalbum:
            album_id = track.album.id
            title = track.album.title
            duration = track.album.duration
            num_tracks = track.album.nb_tracks
            is_explicit = track.album.explicit_lyrics
            release_date = track.album.release_date
            record_type = track.album.record_type
            artist_id  = track.artist.id
            album = api_manager_class.add_album( album_id, title, duration, num_tracks, is_explicit, release_date, \
                     record_type, artist_id)
            db.session.add(album)
            db.session.commit()
           

      # search for track in local DB, add track if not there
    gettrack = api_manager_class.get_track_by_id(track_id)
    if not gettrack:

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

        track = api_manager_class.add_track(track_id, title, duration, is_explicit, audio_preview,\
        release_date, md5_image, track_position,artist_id, album_id) 
        db.session.add(track)
        db.session.commit()

        gettrack = api_manager_class.get_track_by_id(track_id)

        for contributor in track.contributors:
            getcontrib = api_manager_class.get_artist_by_id(contributor.id)
            if not getcontrib:
                artist_id = contributor.id
                name = contributor.name
                artist = api_manager_class.add_artist(artist_id, name)
                db.session.add(artist)
                getcontrib = api_manager_class.get_artist_by_id(contributor.id)
            gettrack.contributors.append(getcontrib)
            db.session.commit()

        
    
        

    likes = likes_manager_class.get_likes_by_id(current_user.id)
    likes.tracks.append(gettrack)

    db.session.commit()
    track = client.get_track(track_id)

    return redirect(f'/api/album/{track.album.id}')

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
    albums = client.get_artist(id).get_albums()

    return render_template('artist.html', artist=artist, toptracks=toptracks, albums=albums)