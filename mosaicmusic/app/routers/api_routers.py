from ..managers.user_manager import user_manager_class
from ..managers.track_manager import track_manager_class

from flask import (
    Blueprint, flash, redirect, render_template, request
)
import deezer

client = deezer.Client(app_id='foo', app_secret='bar')

api_pages = Blueprint('api', __name__, template_folder="templates", url_prefix='/api')


# These routers will be used for viewing and managing  Api - specific information


## Get an album page by ID
@api_pages.get('/album/<int:id>')
def showAlbum(id):

    album = client.get_album(id)
    return render_template('album.html', album=album)

@api_pages.post('/album/<int:id>/<int:trackId>/like/')
def likeTrack(trackId):

    track = client.get_track(trackId)

    track_id = track.id
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

    track_manager_class.add_track(track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id, album_name)

    return redirect('/album/'+ track.album.id)
    
## Get an artist page by ID
@api_pages.get('/artist/<int:id>')
def showArtist(id):

    artist = client.get_artist(id)
    toptracks = client.get_artist(id).get_top()
    return render_template('artist.html', artist=artist, toptracks=toptracks)