from ..models import db, User

# Repository for manipulating User data

class UserManager:
    def create_user(self, email, username, password):
        new_user = User(email, username, password)
        return new_user
    

user_manager_class = UserManager()