from ..models import db, User
from flask_bcrypt import Bcrypt
from ..managers.user_manager import user_manager_class
from ..managers.likes_manager import likes_manager_class
from flask_login import login_user, login_required, current_user,logout_user
import deezer
from flask import (
    Blueprint, flash, redirect, render_template, request
)




client = deezer.Client(app_id='foo', app_secret='bar')
bcrypt = Bcrypt()
auth_pages = Blueprint('auth', __name__, template_folder="templates", url_prefix='')

## These Routers are related to logging a user in and out of an application.


# HOME PAGE ACCESS
@auth_pages.route('/')
def home():
    if not current_user.is_authenticated:
        # Redirect to login or handle it appropriately if user is not authenticated
        return redirect("/login")  # Example redirection to a login page

    albums = client.get_albums_chart(0)
    artists = client.get_artists_chart(0)
    getusers = user_manager_class.get_all_users()

    return render_template('index.html', current_user=current_user, albums=albums, artists=artists, getusers=getusers)


## REGISTER PAGES
@auth_pages.route('/register')
def register():
    return render_template('register.html')  


@auth_pages.post('register')
def register_post():

    ## Get Form Info
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    ## Check if Email Exists
    user = User.query.filter_by(email=email).first()

    if user: # if email exsists, prompt user to try again
        flash('Email address already exists')
        return redirect('/register')
    
    # generate password hash 
    hashed_password = bcrypt.generate_password_hash(password).decode()



    # Create new user in database
    new_user = user_manager_class.create_user(email, username, hashed_password)
    db.session.add(new_user)
    db.session.commit()

    


    return redirect('/login')


## LOGIN PAGES

@auth_pages.route('/login')
def login():
    return render_template('login.html')

@auth_pages.post('/login')
def login_post():

    #Get form information
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    # check if the user actually exists
    user = User.query.filter_by(email=email).first()
    
    # Compare User email and password to what is in the database.
    if not user or not bcrypt.check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect('/login') # if the user doesn't exist or password is wrong, reload the page


    # Log User In
    login_user(user, remember=remember)

    likes = likes_manager_class.get_likes_by_id(current_user.id)

    if not likes:
        likes_id = current_user.id
        id = current_user.id
        new_user_likes = likes_manager_class.create_user_likes(likes_id, id)
        db.session.add(new_user_likes)
        db.session.commit()

        likes = likes_manager_class.get_likes_by_id(current_user.id)


    return redirect('/')


## LOGOUT 
@auth_pages.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You Have Been Logged Out.')
    return redirect('/login')

