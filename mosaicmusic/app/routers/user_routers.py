from ..models import db, User, Likes, Artist
from flask_bcrypt import Bcrypt
from ..managers.user_manager import user_manager_class
from ..managers.likes_manager import likes_manager_class
from ..managers.api_manager import api_manager_class
from werkzeug.utils import secure_filename

import os

import deezer
client = deezer.Client(app_id='foo', app_secret='bar')


from flask_login import  current_user,logout_user

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bcrypt = Bcrypt()
user_pages = Blueprint('user', __name__, template_folder="templates", url_prefix='/my')




## These routers will be used for viewing and managing  user - specific information

@user_pages.route('/account')
def account():

 return render_template('account.html', current_user=current_user)


#picture profile#
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  
@user_pages.post('/account')
def update_user():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    profile_picture = request.files.get('profile_picture') 

    # generate password hash 
    hashed_password = bcrypt.generate_password_hash(password).decode()

    
    profile_picture_filename = None
    if profile_picture and allowed_file(profile_picture.filename):
        # Choose the directory where you want to save the file
      
        profile_picture_filename = secure_filename(profile_picture.filename)
        profile_picture.save(os.path.join('app/static', 'upload_images', profile_picture_filename))
      
    
    # Update User in database
    user_manager_class.update_user(current_user.id, email, username, hashed_password, profile_picture_filename)

    flash('Your account information has been updated.')
    return redirect('/my/account')


@user_pages.post('/account/delete')
def delete_user():
    id = int(current_user.id)
    user_manager_class.delete_user(id)
    logout_user()
    return redirect('/login')



@user_pages.route('/likes')
def likes():

    likes = likes_manager_class.get_likes_by_id(current_user.id)
    artists = Artist.query.get
    mylikes = likes.tracks   

    track_url = ''
    temp = {}

    return render_template('likes.html', current_user=current_user,likes=mylikes, artists=artists,\
                 url_for = url_for, track_url = track_url, temp=temp)

@user_pages.route('/likes/<int:id>')
def trackdetails(id):
    track = client.get_track(id)

    trackobject = track.as_dict()
    
    artists = track.contributors
    album = track.album.title
    releaseDate = track.release_date
    return render_template('song.html', artists=artists, track=track, album=album, releaseDate=releaseDate, trackobject=trackobject)


@user_pages.route('/recommended')
def recspage():
    likes = likes_manager_class.get_likes_by_id(current_user.id)

    mylikes = likes.tracks
    related = []

    for track in mylikes[:3]:
        artist = client.get_artist(track.artist.artist_id)
        related.append(artist.get_related()[:6])

    related
    
    return render_template("recommended.html", related=related)
