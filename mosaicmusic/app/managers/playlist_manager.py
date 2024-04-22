from ..models import db, Likes, Track, Playlist

class PlaylistManager:
    def create_playlist(self, title, descr, picture, user_id):
        new_playlist = Playlist(self, title, descr, picture, user_id)
        return new_playlist
    
    def get_playlist_by_id(self, playlist_id):
        get_playlist = Playlist.query.filter_by(playlist_id=playlist_id).first
        return get_playlist
    
    # def get_playlists_by_user(self, user_id):
    #     get_user_playlists = Playlist.query.filter_by(user_id=user_id).first
    #     return get_user_playlists
    
    def get_playlists_by_user(self, user_id):
        get_user_playlists = Playlist.query.filter_by(user_id=user_id).all()
        return get_user_playlists
    

playlist_manager_class = PlaylistManager()    
