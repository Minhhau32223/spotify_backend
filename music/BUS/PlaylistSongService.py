from music.DAO.PlaylistSongDAO import PlaylistSongDAO

class PlaylistSongService:
    @staticmethod
    def get_all_playlist_songs():
        return PlaylistSongDAO.get_all_playlist_songs()
    @staticmethod
    def get_playlist_song_by_id(playlist_song_id):
        return PlaylistSongDAO.get_playlist_song_by_id(playlist_song_id)
    @staticmethod
    def create_playlist_song(playlist_id, song_id):
        return PlaylistSongDAO.create_playlist_song(playlist_id, song_id)