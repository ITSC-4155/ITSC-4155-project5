from ..models import db, User, Likes

# Repository for manipulating User data

class UserManager:
    def create_user(self, email, username, password):
        new_user = User(email, username, password)
        
        return new_user
    
    def create_user_likes(self, likes_id, id):
        user_likes = Likes(likes_id, id)
        return user_likes
    
    def get_likes_by_id(self, id):
        get_likes = Likes.query.get(id)
        return get_likes


    def get_user_by_id(self, id):
        get_user = User.query.get(id)
        return get_user
    
    

    def update_user(self, id , email , username, password):
        update_user = User.query.get(id)
        update_user.username = username
        update_user.email = email
        update_user.password = password

        db.session.commit()
        return update_user

    def delete_user(self, id):
        user_to_delete = User.query.filter_by(id = id).first_or_404()
        db.session.delete(user_to_delete)
        db.session.commit()
        return user_to_delete

user_manager_class = UserManager()