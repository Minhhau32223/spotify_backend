from rest_framework import serializers
from .models import Song, Album, User, Playlist, PlaylistSong, FavoriteSong, Artist

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
class PlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistSong
        fields = '__all__'

class FavoriteSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteSong
        fields = '__all__'

class artistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

     
        