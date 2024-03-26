
from flask import Flask
from flask_bootstrap import Bootstrap5
from config import Config
from .routers import home_pages, bcrypt
from .models import db


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
bootstrap = Bootstrap5(app)
db.init_app(app)
bcrypt.init_app(app)

  
   
   
    
app.register_blueprint(home_pages)

