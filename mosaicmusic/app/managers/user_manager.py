from ..models import db, User, Likes
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Repository for manipulating User data

class UserManager:
    def create_user(self, email, username, password):
        new_user = User(email, username, password)
        
        return new_user
    

    def get_user_by_id(self, id):
        get_user = User.query.get(id)
        return get_user
    

    def update_user(self, id, email, username, new_password=None, profile_picture=None, about=None):
        user_to_update = User.query.get(id)
        if user_to_update is None:
            return None 

        user_to_update.email = email
        user_to_update.username = username
        
        if new_password is not None:
            hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            user_to_update.password = hashed_password

        if profile_picture is not None:
            user_to_update.profile_picture = profile_picture

        if about is not None:
            user_to_update.about = about

        db.session.commit()
        return user_to_update


    def delete_user(self, id):
        user_to_delete = User.query.filter_by(id = id).first_or_404()
        db.session.delete(user_to_delete)
        db.session.commit()
        return user_to_delete

user_manager_class = UserManager()