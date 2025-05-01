from music.DAO.PlaylistDAO import PlaylistDAO

class PlaylistService:
    @staticmethod
    def get_all_playlists():
        return PlaylistDAO.get_all_playlists()

    @staticmethod
    def get_playlist_by_id(playlist_id):
        return PlaylistDAO.get_playlist_by_id(playlist_id)
