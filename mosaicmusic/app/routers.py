from .models import db, User
from flask_bcrypt import Bcrypt

from .repository import user_repository_singleton

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bcrypt = Bcrypt()
home_pages = Blueprint('home', __name__, template_folder="templates", url_prefix='')


@home_pages.route('/')
def home():
    return render_template('index.html')


@home_pages.route('/register')
def registration():
    return render_template('register.html')
    


@home_pages.post('register')
def register():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    hashed_password = bcrypt.generate_password_hash(password).decode()

    new_user = user_repository_singleton.create_user(email, username, hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/login')
@home_pages.route('/login')
def login():
    return render_template('login.html')