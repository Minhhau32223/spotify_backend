from music.DAO.FavoriteSongDAO import FavoriteSongDAO

class FavoriteSongService:
    @staticmethod
    def get_all_favorite_songs():
        return FavoriteSongDAO.get_all_favorite_songs()
    @staticmethod
    def get_favorite_song_by_id(favorite_song_id):
        return FavoriteSongDAO.get_favorite_song_by_id(favorite_song_id)