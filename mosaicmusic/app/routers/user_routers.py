from ..models import db, User
from flask_bcrypt import Bcrypt
from ..managers.user_manager import user_manager_class
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
   
    return render_template('likes.html', current_user=current_user)

