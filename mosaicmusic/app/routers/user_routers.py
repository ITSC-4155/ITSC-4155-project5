from ..models import db, User
from flask_bcrypt import Bcrypt

from flask_login import login_user, login_required, current_user,logout_user


## These routers will be used for viewing and managing  user - specific information