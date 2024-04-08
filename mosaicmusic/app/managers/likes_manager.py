from ..models import db, User, Likes, Track


class LikesManager:
    def create_user_likes(self, likes_id, id):
        user_likes = Likes(likes_id, id)
        return user_likes
    
    def get_likes_by_id(self, id):
        get_likes = Likes.query.get(id)
        return get_likes

    def get_likes_tracklist_by_id(self, id):
        get_tracklist = Likes.query.filter_by(id = id).all()
        return get_tracklist

likes_manager_class = LikesManager()