
from flask import Flask
from flask_bootstrap import Bootstrap5
from config import Config
from routers.auth_routers import auth_pages, bcrypt
from .models import db, User
from flask_login import LoginManager
login_manager = LoginManager()


# Initializing the app and plugins
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
bootstrap = Bootstrap5(app)
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

  
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(str(user_id)) 
    
app.register_blueprint(auth_pages)

