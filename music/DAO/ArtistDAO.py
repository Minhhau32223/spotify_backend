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
    @staticmethod
    def create_artist(name, bio, profile_image):
        artist = Artist(name=name, bio=bio, profile_image=profile_image)
        artist.save()
        return ArtistDTO(artist.id, artist.name, artist.bio, artist.profile_image)