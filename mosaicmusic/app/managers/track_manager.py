from ..models import db, User, Track

class TrackManager:
    def add_track(self, track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id, album_name):
        new_track = Track(track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id, album_name)
        return new_track
    

track_manager_class = TrackManager()