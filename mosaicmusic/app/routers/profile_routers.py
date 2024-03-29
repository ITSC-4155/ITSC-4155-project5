from ..models import db, User

from ..managers.user_manager import user_manager_class
from flask_login import login_user, login_required, current_user,logout_user

from flask import (
    Blueprint, flash, redirect, render_template, request
)


profile_pages = Blueprint('profile', __name__, template_folder="templates", url_prefix='/profiles')


## These routers will be used for viewing and managing  profile page - specific information

@profile_pages.get('/<int:id>')
def get_profile(id):
    fetch_user = user_manager_class.get_user_by_id(id)
    return render_template('profile.html', user=fetch_user)

@profile_pages.get('/<int:id>/edit')
def edit_profile(id):
    fetch_user = user_manager_class.get_user_by_id(id)
    return render_template('account.html', user=fetch_user)

