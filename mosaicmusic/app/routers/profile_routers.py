from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from ..models import db, User
from ..managers.user_manager import user_manager_class
from flask_bcrypt import Bcrypt
import os
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, abort
)

bcrypt = Bcrypt()
profile_pages = Blueprint('profile', __name__, template_folder="templates", url_prefix='/profiles')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@profile_pages.get('/<int:id>')
def get_profile(id):
    fetch_user = user_manager_class.get_user_by_id(id)
    return render_template('profile.html', user=fetch_user)

# Route to show the edit profile form
@profile_pages.route('/<int:id>/edit', methods=['GET'])
@login_required
def show_edit_profile(id):
    if current_user.id != id:
        abort(403)  
    user_to_edit = user_manager_class.get_user_by_id(id)
    return render_template('edit_profile.html', user=user_to_edit)


@profile_pages.get('/all')
def all_profiles():
    getusers = user_manager_class.get_all_users()
    return render_template('all_users.html', getusers=getusers)


# Route to process the edit profile form submission
@profile_pages.route('/<int:id>/edit', methods=['POST'])
@login_required
def edit_profile(id):
    if current_user.id != id:
        abort(403)  

    
    new_password = None

    user_to_edit = user_manager_class.get_user_by_id(id)
    if not user_to_edit:
        flash('User not found.')
        return redirect(url_for('main.index'))  

    username = request.form.get('username')
    email = request.form.get('email')
    new_password = request.form.get('password') 

    # Check if a new password was provided and hash it
    new_password_hash = None
    if new_password:
        new_password_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')

    # Handle the profile picture update
    profile_picture = request.files.get('profile_picture')
    profile_picture_filename = None
    if profile_picture and allowed_file(profile_picture.filename):
        filename = secure_filename(profile_picture.filename)
        filepath = os.path.join('app/static/upload_images/profile', filename)
        profile_picture.save(filepath)
        profile_picture_filename = filename  

    user_manager_class.update_user(id, email, username, new_password_hash, profile_picture_filename)

    db.session.commit()
    flash('Profile updated successfully!')
    return redirect(url_for('profile.get_profile', id=id))
