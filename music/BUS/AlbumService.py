from music.DAO.AlbumDAO import AlbumDAO
from music.DAO.SongDAO import SongDAO
class AlbumService:
    @staticmethod
    def get_all_albums():
        return AlbumDAO.get_all_albums()

    @staticmethod
    def get_album_by_id(album_id):
        return AlbumDAO.get_album_by_id(album_id)
    @staticmethod
    def get_songs_in_album(album_id):
        # Truy vấn các bài hát của album từ cơ sở dữ liệu
        return SongDAO.objects.filter(album_id=album_id)
    @staticmethod
    def create_album(name, description, image, bg_color):
        return AlbumDAO.create_album(name, description, image, bg_color)