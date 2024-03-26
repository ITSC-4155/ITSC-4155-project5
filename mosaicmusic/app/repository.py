from .models import db, User

class UserRepository:
    def create_user(self, email, username, password):
        new_user = User(email, username, password)
        return new_user
    

user_repository_singleton = UserRepository()