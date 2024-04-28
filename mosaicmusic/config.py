import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    """All application configurations"""


    # Secret key

    SECRET_KEY = os.environ.get('SECRET_KEY')

    
    # Database configurations
    if os.getenv('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance', 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    UPLOAD_FOLDER = 'static/images'
