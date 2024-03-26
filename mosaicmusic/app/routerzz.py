# from .models import db, User
# from flask_bcrypt import Bcrypt
# from .repository import user_repository_singleton
# from flask_login import login_user, login_required, current_user,logout_user

# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, session, url_for
# )


# bcrypt = Bcrypt()
# home_pages = Blueprint('home', __name__, template_folder="templates", url_prefix='')



# # AUTH ROUTERS


# @home_pages.route('/register')
# def register():
#     return render_template('register.html')  


# @home_pages.post('register')
# def register_post():
#     email = request.form.get('email')
#     username = request.form.get('username')
#     password = request.form.get('password')

#     user = User.query.filter_by(email=email).first()

#     if user: # if a user is found, we want to redirect back to signup page so user can try again
#         flash('Email address already exists')
#         return redirect('/register')
    
#     hashed_password = bcrypt.generate_password_hash(password).decode()
#     new_user = user_repository_singleton.create_user(email, username, hashed_password)
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect('/login')


# @home_pages.route('/login')
# def login():
#     return render_template('login.html')

# @home_pages.post('/login')
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     remember = True if request.form.get('remember') else False
    
#     # check if the user actually exists
#     user = User.query.filter_by(email=email).first()
    
#     # take the user-supplied password, hash it, and compare it to the hashed password in the database
#     if not user or not bcrypt.check_password_hash(user.password, password):
#         flash('Please check your login details and try again.')
#         return redirect('/login') # if the user doesn't exist or password is wrong, reload the page


#     # if the above check passes, then we know the user has the right credentials
#     login_user(user, remember=remember)
#     return redirect('/')

# @home_pages.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You Have Been Logged Out.')
#     return redirect('/login')


# # HOME ROUTERS
# @home_pages.route('/')
# def home():

#     if current_user.is_authenticated == True:
#         user = current_user.username
#     else:
#         user = None

#     return render_template('index.html', username=user)