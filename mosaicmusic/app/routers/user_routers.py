from ..models import db, User, Likes
from flask_bcrypt import Bcrypt
from ..managers.user_manager import user_manager_class
from ..managers.likes_manager import likes_manager_class
from ..managers.track_manager import track_manager_class


from flask_login import login_user, login_required, current_user,logout_user

from flask import (
    Blueprint, flash, redirect, render_template, request
)

bcrypt = Bcrypt()
user_pages = Blueprint('user', __name__, template_folder="templates", url_prefix='/my')



## These routers will be used for viewing and managing  user - specific information

@user_pages.route('/account')
def account():

 return render_template('account.html', current_user=current_user)


@user_pages.post('/account')
def update_user():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')   

    # generate password hash 
    hashed_password = bcrypt.generate_password_hash(password).decode()

    # Update User in database
    user_manager_class.update_user(current_user.id, email, username, hashed_password)

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
    
    likes = Likes.query.filter_by(id=current_user.id).first()

    if not likes:
        likes_id = current_user.id
        id = current_user.id
        new_user_likes = likes_manager_class.create_user_likes(likes_id, id)
        db.session.add(new_user_likes)
        db.session.commit()

    mylikes = likes.tracks

    

    return render_template('likes.html', current_user=current_user, likes=mylikes)

