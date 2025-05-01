from music.models import PlaylistSong
from music.DTO.PlaylistSongDTO import PlaylistSongDTO

class PlaylistSongDAO:
    @staticmethod
    def get_all_playlist_songs():
        playlist_songs = PlaylistSong.objects.all()
        return [PlaylistSongDTO(ps.id, ps.playlist_id, ps.song_id) for ps in playlist_songs]
    def get_playlist_song_by_id(playlist_song_id):
        ps = PlaylistSong.objects.filter(id=playlist_song_id).first()
        return PlaylistSongDTO(ps.id, ps.playlist_id, ps.song_id) if ps else None