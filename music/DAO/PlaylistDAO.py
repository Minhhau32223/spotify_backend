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
