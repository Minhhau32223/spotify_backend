from music.models import FavoriteSong
from music.DTO.FavoriteSongDTO import FavoriteSongDTO

class FavoriteSongDAO:
    @staticmethod
    def get_all_favorite_songs():
        favorites = FavoriteSong.objects.all()
        return [FavoriteSongDTO(f.id, f.user_id, f.song_id) for f in favorites]

    @staticmethod
    def get_favorite_song_by_id(favorite_song_id):
        f = FavoriteSong.objects.filter(id=favorite_song_id).first()
        return FavoriteSongDTO(f.id, f.user_id, f.song_id) if f else None