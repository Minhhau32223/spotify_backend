from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.FavoriteSong import FavoriteSongService

@api_view(['GET'])
def get_all_favorite_songs(request):
    favorite_songs = FavoriteSongService.get_all_favorite_songs()
    return Response([fs.__dict__ for fs in favorite_songs])

@api_view(['GET'])
def get_favorite_song_detail(request, fs_id):
    favorite_song = FavoriteSongService.get_favorite_song_by_id(fs_id)
    return Response(favorite_song.__dict__) if favorite_song else Response({'error': 'Not found'}, status=404)
