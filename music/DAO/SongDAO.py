from music.models import Song
from music.DTO.SongDTO import SongDTO

class SongDAO:
    @staticmethod
    def get_all_songs():
        songs = Song.objects.all()
        return [SongDTO(s.id, s.name, s.file, s.image, s.desc, s.duration, s.album_id, s.artist_id) for s in songs]

    @staticmethod
    def get_song_by_id(song_id):
        s = Song.objects.filter(id=song_id).first()
        return SongDTO(s.id, s.name, s.file, s.image, s.desc, s.duration, s.album_id, s.artist_id) if s else None

    @staticmethod
    def get_songs_in_album(album_id):
        # Truy vấn các bài hát của album từ cơ sở dữ liệu
        songs = Song.objects.filter(album_id=album_id)
        return [SongDTO(s.id, s.name, s.file, s.image, s.desc, s.duration, s.album_id, s.artist_id) for s in songs]
    def get_songs_in_playlist(playlist_id):
        # Truy vấn các bài hát của playlist từ cơ sở dữ liệu
        songs = Song.objects.filter(playlist_id=playlist_id)
        return [SongDTO(s.id, s.name, s.file, s.image, s.desc, s.duration, s.album_id, s.artist_id) for s in songs]