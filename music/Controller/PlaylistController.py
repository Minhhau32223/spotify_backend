from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.PlaylistService import PlaylistService

@api_view(['GET'])
def get_all_playlists(request):
    playlists = PlaylistService.get_all_playlists()
    return Response([playlist.__dict__ for playlist in playlists])

@api_view(['GET'])
def get_playlist_detail(request, playlist_id):
    playlist = PlaylistService.get_playlist_by_id(playlist_id)
    return Response(playlist.__dict__) if playlist else Response({'error': 'Not found'}, status=404)
