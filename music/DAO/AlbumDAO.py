from music.models import Album
from music.DTO.AlbumDTO import AlbumDTO

class AlbumDAO:
    @staticmethod
    def get_all_albums():
        albums = Album.objects.all()
        return [AlbumDTO(a.id, a.name, a.image, a.description, a.bg_color) for a in albums]

    @staticmethod
    def get_album_by_id(album_id):
        a = Album.objects.filter(id=album_id).first()
        return AlbumDTO(a.id, a.name, a.image, a.description, a.bg_color) if a else None
