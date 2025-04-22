from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Album, Song, Playlist, PlaylistSong, FavoriteSong  , Artist
from .serializers import UserSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer, PlaylistSongSerializer, FavoriteSongSerializer,artistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = artistSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistSongViewSet(viewsets.ModelViewSet):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer
class FavoriteSongViewSet(viewsets.ModelViewSet):
    queryset = FavoriteSong.objects.all()
    serializer_class = FavoriteSongSerializer



class SongsInAlbumView(ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        album_id = self.kwargs['album_id']
        return Song.objects.filter(album_id=album_id)

# Create your views here.
