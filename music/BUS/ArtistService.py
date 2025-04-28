from music.DAO.ArtistDAO import ArtistDAO

class ArtistService:
    @staticmethod
    def get_all_artists():
        return ArtistDAO.get_all_artists()

    @staticmethod
    def get_artist_by_id(artist_id):
        return ArtistDAO.get_artist_by_id(artist_id)
