class SongDTO:
    def __init__(self, id, name, file, image, desc, duration, album_id, artist_id):
        self.id = id
        self.name = name
        self.file = file
        self.image = image
        self.desc = desc
        self.duration = duration
        self.album_id = album_id
        self.artist_id = artist_id
