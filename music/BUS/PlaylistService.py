from music.DAO.PlaylistDAO import PlaylistDAO

class PlaylistService:
    @staticmethod
    def get_all_playlists():
        return PlaylistDAO.get_all_playlists()

    @staticmethod
    def get_playlist_by_id(playlist_id):
        return PlaylistDAO.get_playlist_by_id(playlist_id)
    @staticmethod
    def create_playlist(name, user_id):
        return PlaylistDAO.create_playlist(name, user_id)
    @staticmethod
    def get_playlists_by_user_id(user_id):
        return PlaylistDAO.get_playlists_by_user_id(user_id)
