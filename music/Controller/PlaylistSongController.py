from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.PlaylistSongService import PlaylistSongService

@api_view(['GET'])
def get_all_playlist_songs(request):
    playlist_songs = PlaylistSongService.get_all_playlist_songs()
    return Response([ps.__dict__ for ps in playlist_songs])

@api_view(['GET'])
def get_playlist_song_detail(request, ps_id):
    playlist_song = PlaylistSongService.get_playlist_song_by_id(ps_id)
    return Response(playlist_song.__dict__) if playlist_song else Response({'error': 'Not found'}, status=404)
