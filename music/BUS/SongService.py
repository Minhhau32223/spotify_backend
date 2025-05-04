from music.DAO.SongDAO import SongDAO

class SongService:
    @staticmethod
    def get_all_songs():
        return SongDAO.get_all_songs()

    @staticmethod
    def get_song_by_id(song_id):
        return SongDAO.get_song_by_id(song_id)

    @staticmethod
    def get_songs_in_album(album_id):
  
        return SongDAO.get_songs_in_album(album_id)
    def get_songs_in_playlist(playlist_id):
    
        return SongDAO.get_songs_in_playlist(playlist_id)
    @staticmethod
    def create_song(name, file, image, desc, duration, album_id, artist_id):
        return SongDAO.create_song(name, file, image, desc, duration, album_id, artist_id)