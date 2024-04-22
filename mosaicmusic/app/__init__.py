from flask import Flask
from flask_bootstrap import Bootstrap5
from config import Config
from deezer import Client

from .routers import auth_routers, user_routers, profile_routers, search_routers, api_routers, playlist_routers

from .models import db, User
from flask_login import LoginManager


client = Client()
login_manager = LoginManager()



# Initializing the app and plugins
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)


bootstrap = Bootstrap5(app)
db.init_app(app)
auth_routers.bcrypt.init_app(app)
login_manager.init_app(app)

  
login_manager.login_view = 'auth.login'





@login_manager.user_loader
def load_user(id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(id) 


app.register_blueprint(auth_routers.auth_pages)
app.register_blueprint(user_routers.user_pages)
app.register_blueprint(profile_routers.profile_pages)
app.register_blueprint(search_routers.search_blueprint)
app.register_blueprint(api_routers.api_pages)
app.register_blueprint(playlist_routers.playlist_blueprint)
