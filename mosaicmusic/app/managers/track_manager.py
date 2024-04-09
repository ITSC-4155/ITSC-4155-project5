from ..models import db, User, Track

class TrackManager:
    def add_track(self, track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id, album_name):
        new_track = Track(track_id, title, duration, is_explicit, audio_preview,\
      release_date, md5_image, track_position,artist_id, album_id, album_name)
        return new_track
    
    def get_track_by_id(self, track_id):
        get_track = Track.query.get(track_id)
        return get_track
    
track_manager_class = TrackManager()

class Duration:
  def convert(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60 
    return "%02d:%02d" % (minutes, seconds)

duration = Duration()