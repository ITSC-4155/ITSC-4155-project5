from ..models import db,  Track, Album, Artist

class ApiManager:
    def add_track(self, track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id):
        new_track = Track(track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id)
      
        return new_track
    
    
    def get_track_by_id(self, track_id):
        get_track = Track.query.get(track_id)
        return get_track
    
    def add_album(self, album_id, title, duration, num_tracks, is_explicit, release_date, \
                     record_type, artist_id ):
        new_album = Album( album_id, title, duration, num_tracks, is_explicit, release_date, \
                     record_type, artist_id )
        return new_album
    
    def get_album_by_id(self, album_id):
        get_album = Track.query.filter_by(album_id=album_id).first()
        return get_album


    def add_artist(self, artist_id, name ):
        new_artist = Artist(artist_id, name)
        db.session.add(new_artist)
        return new_artist
    
    def get_artist_by_id(self, artist_id):
        get_artist = Track.query.filter_by(artist_id=artist_id).first()
        return get_artist

api_manager_class = ApiManager()
