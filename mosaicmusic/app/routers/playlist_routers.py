from ..models import Playlist, db
from ..managers.playlist_manager import playlist_manager_class
from ..managers.likes_manager import likes_manager_class
from ..managers.api_manager import api_manager_class


from flask_login import  current_user,logout_user
from flask import (
    Blueprint, g, render_template
)
from ..managers.playlist_manager import playlist_manager_class

import deezer

client = deezer.Client(app_id='foo', app_secret='bar')

from werkzeug.utils import secure_filename
import os

playlist_blueprint = Blueprint('playlist', __name__, template_folder="templates", url_prefix='/playlists')

@playlist_blueprint.route("/<int:id>")
def get_playlist(id):
    
    fetch_playlist = playlist_manager_class.get_playlist_by_id(id)
    likes = likes_manager_class.get_likes_by_id(current_user.id)
    mylikes = likes.tracks

    return render_template("playlist.html", playlist=fetch_playlist, likes = mylikes)


#picture profile#
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@playlist_blueprint.route("/create")
def create_playlist_page():


    return render_template("create_playlist.html")

@playlist_blueprint.post("create")
def create_playlist():

    title = request.form.get('title')
    descr = request.form.get('description')
    playlist_picture = request.files.get('picture')
    user_id = current_user.id
    

    playlist_picture_filename = None
    if playlist_picture and allowed_file(playlist_picture.filename):
        # Choose the directory where you want to save the file
      
        playlist_picture_filename = secure_filename(playlist_picture.filename)
        playlist_picture.save(os.path.join('app/static', 'upload_images', playlist_picture_filename))
    
    else:
        playlist_picture_filename = "iphone.jpg"

    new_playlist = playlist_manager_class.create_playlist(title, descr, playlist_picture_filename, user_id)
    db.session.add(new_playlist)
    db.session.commit()
    return redirect("/")


@playlist_blueprint.route("/<int:id>/edit")
def show_edit_playlist(id):

    playlist = playlist_manager_class.get_playlist_by_id(id)
    return render_template("edit_playlist.html", playlist=playlist)


@playlist_blueprint.post("/<int:id>/edit")
def edit_playlist(id):

    title = request.form.get('title')
    descr = request.form.get('description')
    playlist_picture = request.files.get('picture')
    playlist_id = id
    

    playlist_picture_filename = None
    if playlist_picture and allowed_file(playlist_picture.filename):
        # Choose the directory where you want to save the file
      
        playlist_picture_filename = secure_filename(playlist_picture.filename)
        playlist_picture.save(os.path.join('app/static', 'upload_images', playlist_picture_filename))
    
    else:
        playlist_picture_filename = "iphone.jpg"

    update_playlist = playlist_manager_class.update_playlist(id, title, descr, playlist_picture_filename)
    db.session.add(update_playlist)
    db.session.commit()

    return redirect(f'/playlists/{id}')



@playlist_blueprint.post('/<int:id>/add/<int:track_id>')
def add_track(id, track_id):

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

    playlist = playlist_manager_class.get_playlist_by_id(id)
    playlist.tracks.append(gettrack)

    db.session.commit()
    

    return redirect(f'/playlists/{id}')


@playlist_blueprint.post('/<int:id>/remove/<int:track_id>')
def remove_track(id, track_id):


    gettrack = api_manager_class.get_first_track(track_id)
    playlist = playlist_manager_class.get_playlist_by_id(id)
    playlist.tracks.remove(gettrack)

    db.session.commit()
    return redirect(f'/playlists/{id}')


# @playlist_blueprint.route("/playlists/<int:playlist_id>")
# def show_playlist(playlist_id):
#     """Show detail on specific playlist."""

#     # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
#     playlist = Playlist.query.get_or_404(playlist_id)
#     return render_template("playlist.html", playlist=playlist)


# @playlist_blueprint.route("/playlists/add", methods=["GET", "POST"])
# def add_playlist():
#     # """Handle add-playlist form:

#     # - if form not filled out or invalid: show form
#     # - if valid: add playlist to SQLA and redirect to list-of-playlists
#     # """

#     # # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
#     # form = PlaylistForm()
#     # if form.validate_on_submit():
#     #     name = form.name.data
#     #     description = form.description.data

#     #     new_playlist = Playlist(name=name, description=description)
#     #     db.session.add(new_playlist)
#     #     db.session.commit()
#     #     return redirect("/playlists")

#     return render_template("new_playlist.html", )