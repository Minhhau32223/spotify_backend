from music.models import Playlist
from music.DTO.PlaylistDTO import PlaylistDTO

class PlaylistDAO:
    @staticmethod
    def get_all_playlists():
        playlists = Playlist.objects.all()
        return [PlaylistDTO(p.id, p.name, p.user_id) for p in playlists]

    @staticmethod
    def get_playlist_by_id(playlist_id):
        p = Playlist.objects.filter(id=playlist_id).first()
        return PlaylistDTO(p.id, p.name, p.user_id) if p else None
    @staticmethod
    def create_playlist(name, user_id):
        playlist = Playlist(name=name, user_id=user_id)
        playlist.save()
        return PlaylistDTO(playlist.id, playlist.name, playlist.user_id)
    @staticmethod
    def get_playlists_by_user_id(user_id):
        playlists = Playlist.objects.filter(user_id=user_id)
        return [PlaylistDTO(p.id, p.name, p.user_id) for p in playlists]
