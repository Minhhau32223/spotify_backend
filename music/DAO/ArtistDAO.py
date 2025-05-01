from music.models import Artist
from music.DTO.ArtistDTO import ArtistDTO

class ArtistDAO:
    @staticmethod
    def get_all_artists():
        artists = Artist.objects.all()
        return [ArtistDTO(a.id, a.name, a.bio, a.profile_image) for a in artists]

    @staticmethod
    def get_artist_by_id(artist_id):
        a = Artist.objects.filter(id=artist_id).first()
        return ArtistDTO(a.id, a.name, a.bio, a.profile_image) if a else None
