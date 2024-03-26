from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile_picture = db.Column(db.String, nullable=True)
    about = db.Column(db.String, nullable=True) 
   
    
    def __init__(self, email, username, password) -> None:
        self.email = email
        self.username = username
        self.password = password
        self.profile_picture = ''
        self.about = ''